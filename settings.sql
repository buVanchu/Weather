-- SCHEMA: weather

-- DROP SCHEMA IF EXISTS weather ;

CREATE SCHEMA IF NOT EXISTS weather
    AUTHORIZATION postgres;

-- Table: weather.power_prediction

-- DROP TABLE IF EXISTS weather.power_prediction;

CREATE TABLE IF NOT EXISTS weather.power_prediction
(
    id bigint NOT NULL DEFAULT nextval('weather.power_prediction_id_seq'::regclass),
    power real,
    data date,
    CONSTRAINT power_prediction_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS weather.power_prediction
    OWNER to postgres;

-- FUNCTION: weather.update_or_insert_data(date, real)

-- DROP FUNCTION IF EXISTS weather.update_or_insert_data(date, real);

CREATE OR REPLACE FUNCTION weather.update_or_insert_data(
  date_param date,
  power_param real)
    RETURNS void
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
BEGIN
    IF EXISTS (SELECT 1 FROM weather.power_prediction WHERE data = date_param) THEN
        UPDATE weather.power_prediction
        SET power = power_param
        WHERE data = date_param;
    ELSE
        INSERT INTO weather.power_prediction (data, power)
        VALUES (date_param, power_param);
    END IF;
END;
$BODY$;

ALTER FUNCTION weather.update_or_insert_data(date, real)
    OWNER TO postgres;