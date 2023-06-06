-- grant privileges for the user
grant all privileges on flight_delay.* to 'kafka';

-- change datatype of 'EntryDate' column to datetime
alter table flight reocrds modify EntryDate datetime;