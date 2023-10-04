CREATE OR REPLACE FUNCTION public.update_or_insert_data_cons(
	date_param date,
	power_param double precision)
    RETURNS void
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
BEGIN
    IF EXISTS (SELECT 1 FROM predicted_power WHERE date_stamp = date_param) THEN
        UPDATE predicted_power
        SET consumed_power = power_param
        WHERE date_stamp = date_param;
    ELSE
        INSERT INTO predicted_power (date_stamp, consumed_power, user_id)
        VALUES (date_param, power_param, 1);
    END IF;
END;
$BODY$;