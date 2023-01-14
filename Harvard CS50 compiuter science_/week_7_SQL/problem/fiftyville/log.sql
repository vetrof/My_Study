-- Keep a log of any SQL queries you execute as you solve the mystery.

--ищем в полицейской сводке события за 28 июля 2021 года на 'Humphrey Street'
select * from crime_scene_reports
where year = 2021
  and month = 7
  and day = 28
  and street = 'Humphrey Street';
--результат: id 295 Кража утки CS50 произошла в 10:15 на улице Хамфри.
-- Сегодня были проведены допросы трех свидетелей, которые присутствовали
---- в то время -- пекарня упоминается в каждой из стенограмм их интервью.
-- пекарня - bakery



-- ищем а базе интервью по дате и ключевому слову bakery
select * from interviews
where year = 2021
  and month = 7
  and day = 28
  and transcript like '%bakery%';
--  Где-то через десять минут после кражи я увидел, как вор сел в машину
-- на стоянке пекарни и уехал. Если у вас есть видеозаписи с парковки пекарни,
--  вы можете поискать автомобили, которые покинули парковку в этот период времени

--Я не знаю имени вора, но я узнал его. Сегодня утром, прежде чем я пришел в
--пекарню Эммы, я проходил мимо банкомата на Леггетт-стрит и увидел там вора,
--снимающего деньги.

--Когда вор выходил из пекарни, они позвонили кому-то, кто разговаривал
--с ними менее минуты. Во время разговора я услышал, как вор сказал,
--что они планируют вылететь завтра самым ранним рейсом из Фифтивилля.
--Затем вор попросил человека на другом конце телефона купить билет на самолет.


-- поищем в видеозаписях какие машины уехали с парковки в период 10:15 ам + примерно 10 минут
SELECT license_plate FROM bakery_security_logs
where year = 2021
  and month = 7
  and day = 28
  and hour = 10
  and minute > 20
  and activity = 'exit';
--  примерно в это время выехало три машины c парковки пекарни
--  10:21 L93JTIZ
--  10:23 322W7JE
--  10:23 0NTHK55


-- поищем кто мог снимать в это время деньги с банкомата
--получаем банковские аккаунты кто снимал в этот день деньги
SELECT account_number FROM atm_transactions
where year = 2021
  and month = 7
  and day = 28
  and atm_location = 'Leggett Street'
  and transaction_type = 'withdraw';

--  поищем person ID  и другую инфу по этим аккаунтам в базе банка
--и связанной с ним базе по людям
SELECT *  FROM bank_accounts
JOIN people ON bank_accounts.person_id = people.id
WHERE account_number IN(SELECT account_number FROM atm_transactions
                        where year = 2021
                          and month = 7
                          and day = 28
                          and atm_location = 'Leggett Street'
                          and transaction_type = 'withdraw');

--поищем разные пересечения по номерам машин
SELECT license_plate FROM bakery_security_logs
where year = 2021
  and month = 7
  and day = 28
  and hour = 10
  and minute > 22
  and activity = 'exit'
INTERSECT
SELECT license_plate  FROM bank_accounts
JOIN people ON bank_accounts.person_id = people.id
WHERE account_number IN(SELECT account_number FROM atm_transactions
                        where year = 2021
                          and month = 7
                          and day = 28
                          and atm_location = 'Leggett Street'
                          and transaction_type = 'withdraw';
--получаем два номера автомобиля  1106N58 322W7JE

--ищем владельцев и другую информацию по номеру авто
SELECT * from people
WHERE license_plate = '1106N58' OR license_plate = '322W7JE';
--результаты на основе номера машин со стоянки и информации из банкомата
--449774	Taylor	(286) 555-6063	1988161715	1106N58
--514354	Diana	(770) 555-1861	3592750733	322W7JE


-- нужно проверить не говорил ли кто из этих номеров во время ограбления и с кем они говорили
SELECT * FROM people
WHERE phone_number = (
SELECT receiver FROM phone_calls
where year = 2021
and month = 7
and day = 28
and duration < 60
and caller = '(286) 555-6063');
--получаем что
--449774	Taylor	(286) 555-6063	1988161715	1106N58 говорил с
--250277	James	(676) 555-6554	2438825627	Q13SVG6

SELECT * FROM people
WHERE phone_number = (725) 555-3243;
--WHERE phone_number = (
SELECT * FROM phone_calls
where year = 2021
and month = 7
and day = 28
and duration < 60
and caller = '(770) 555-1861';
-- получаем что
--514354	Diana	(770) 555-1861	3592750733	322W7JE звонила абоненту
--которого нет в базе --(725) 555-3243

--поищем в базе номера которые звонили друг другу менее минуты
SELECT * FROM phone_calls
where year = 2021
and month = 7
and day = 28
and duration < 60;

--найдем самый ранний рейс на следующий день после похищения - 29го
SELECT * FROM airports;
-- код аэропорта фифтивилля CSF 8

SELECT SELECT * FROM airports
JOIN flights ON airports.id = flights.origin_airport_id
JOIN passengers ON flights.id = passengers.flight_id
JOIN people ON passengers.passport_number = people.passport_number
where year = 2021
and month = 7
and day = 29
and abbreviation = 'CSF'
and hour = 8;
-- самый ранний рейс
--8	CSF	Fiftyville Regional Airport	Fiftyville	36	8	4	2021	7	29	8	20
-- в 8 20 из фифтивилля в LGA	LaGuardia Airport	New York City id рейса - 36

--данные всех кто летел этим рейсом из базы
--2A	953679	Doris	(066) 555-9701	7214083635	M51FA04
--3B	398010	Sofia	(130) 555-0289	1695452385	G412CB7
--4A	686048	Bruce	(367) 555-5533	5773159633	94KL13X
--5C	651714	Edward	(328) 555-1152	1540955065	130LD9Z
--6C	560886	Kelsey	(499) 555-9472	8294398571	0NTHK55
--6D	449774	Taylor	(286) 555-6063	1988161715	1106N58
--7A	395717	Kenny	(826) 555-1652	9878712108	30G67EN
--7B	467400	Luca	(389) 555-5198	8496433585	4328GD8

-- на данный момент получается что вор 6D 449774	Taylor	(286) 555-6063	1988161715	1106N58
--рядом с ним сидела 6C	560886	Kelsey	(499) 555-9472	8294398571	0NTHK55
--проверим ее звонки

SELECT * FROM phone_calls
JOIN people ON phone_calls.receiver = people.phone_number
WHERE caller = '(286) 555-6063';



--расследование зашло в тупик
--начнем расследование по новому кругу




-- Соединим список тех кто снимал деньги с банкомата и  список пассажиров
SELECT name FROM airports
JOIN flights ON airports.id = flights.origin_airport_id
JOIN passengers ON flights.id = passengers.flight_id
JOIN people ON passengers.passport_number = people.passport_number
where year = 2021
and month = 7
and day = 29
and abbreviation = 'CSF'
and hour = 8
intersect
SELECT name
  FROM people
  JOIN bank_accounts ON people.id = bank_accounts.person_id
  JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
 WHERE atm_transactions.year = 2021
   AND atm_transactions.month = 7
   AND atm_transactions.day = 28
   AND atm_transactions.atm_location = 'Leggett Street'
   AND atm_transactions.transaction_type = 'withdraw';
--получаем список подозреваемых
--Bruce
--Kenny
--Luca
--Taylor

--Проверим кто в этот день звонил меньше 60 сек
SELECT name, phone_calls.duration
  FROM people
  JOIN phone_calls
    ON people.phone_number = phone_calls.caller
 WHERE phone_calls.year = 2021
   AND phone_calls.month = 7
   AND phone_calls.day = 28
   AND phone_calls.duration <= 60
 ORDER BY phone_calls.duration;
-- Kelsey	36
--Carina	38
--Taylor	43
--Bruce	45
--Diana	49
--Kelsey	50
--Sofia	51
--Benista	54
--Kenny	55
--Kathryn	60

--Проверим кто в этот день принимал звонки меньше 60 сек
SELECT name, phone_calls.duration
  FROM people
  JOIN phone_calls
    ON people.phone_number = phone_calls.receiver
 WHERE phone_calls.year = 2021
   AND phone_calls.month = 7
   AND phone_calls.day = 28
   AND phone_calls.duration <= 60
   ORDER BY phone_calls.duration;
-- Larry	36
--Jacqueline	38
--James	43
--Robin	45
--Philip	49
--Melissa	50
--Jack	51
--Anna	54
--Doris	55
--Luca	60

--Luca	звонила  Kathryn
--Bruce  звонил  Robin

--проверим кто выезжал со стоянки у пекарни в указанное время
SELECT name, bakery_security_logs.hour, bakery_security_logs.minute FROM people
  JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate
 WHERE bakery_security_logs.year = 2021
   AND bakery_security_logs.month = 7
   AND bakery_security_logs.day = 28
   AND bakery_security_logs.activity = 'exit'
   AND bakery_security_logs.hour = 10
   AND bakery_security_logs.minute >= 15
   AND bakery_security_logs.minute <= 30
 ORDER BY bakery_security_logs.minute;
--Vanessa 10	16
--Bruce	  10	18 +
--Barry	  10	18
--Luca	  10	19 +
--Sofia	  10	20
--Iman	  10	21
--Diana	  10	23
--Kelsey  10	23

--Круг подозреваемых, они снимали деньги, летели рейсом, выезжали с парковки
--Bruce	  10	18 +
--Luca	  10	19 +

--Luca	звонила  Kathryn
--Bruce  звонил  Robin


--по всем описаниям подходит два человека Bruce и Luca
--Но если поверить свидетелю и предположить что именно грабитель делал
--исходящий звонок - то выходит что грабитель Bruce и его сообщник Robin