WITH week_activities AS (
    SELECT
        c.id,
        c.title,
        c.rate,
        TIMESTAMPDIFF(MINUTE, a.start_dt, a.end_dt) as minutes,
        DAYOFWEEK(a.start_dt) as day_num
    FROM contracts c
    JOIN activities a ON c.id = a.contract_id
    WHERE a.start_dt >= '2022-06-13' AND a.start_dt < '2022-06-20'
),
contract_summary AS (
    SELECT
        id,
        title,
        rate,
        SUM(CASE WHEN day_num = 2 THEN minutes ELSE 0 END) as mon_min,
        SUM(CASE WHEN day_num = 3 THEN minutes ELSE 0 END) as tue_min,
        SUM(CASE WHEN day_num = 4 THEN minutes ELSE 0 END) as wed_min,
        SUM(CASE WHEN day_num = 5 THEN minutes ELSE 0 END) as thu_min,
        SUM(CASE WHEN day_num = 6 THEN minutes ELSE 0 END) as fri_min,
        SUM(CASE WHEN day_num = 7 THEN minutes ELSE 0 END) as sat_min,
        SUM(CASE WHEN day_num = 1 THEN minutes ELSE 0 END) as sun_min,
        SUM(minutes) as total_minutes
    FROM week_activities
    GROUP BY id, title, rate
),
final_result AS (
    SELECT
        id,
        title,
        CONCAT(FLOOR(mon_min / 60), ':', LPAD(mon_min % 60, 2, '0')) as mon,
        CONCAT(FLOOR(tue_min / 60), ':', LPAD(tue_min % 60, 2, '0')) as tue,
        CONCAT(FLOOR(wed_min / 60), ':', LPAD(wed_min % 60, 2, '0')) as wed,
        CONCAT(FLOOR(thu_min / 60), ':', LPAD(thu_min % 60, 2, '0')) as thu,
        CONCAT(FLOOR(fri_min / 60), ':', LPAD(fri_min % 60, 2, '0')) as fri,
        CONCAT(FLOOR(sat_min / 60), ':', LPAD(sat_min % 60, 2, '0')) as sat,
        CONCAT(FLOOR(sun_min / 60), ':', LPAD(sun_min % 60, 2, '0')) as sun,
        CONCAT(FLOOR(total_minutes / 60), ':', LPAD(total_minutes % 60, 2, '0')) as hours,
        rate,
        CONCAT('$', FORMAT((total_minutes / 60.0) * CAST(REPLACE(REPLACE(rate, '$', ''), '/hr', '') AS DECIMAL(10,2)), 2)) as amount
    FROM contract_summary

    UNION ALL

    SELECT
        999999,
        NULL,
        CONCAT(FLOOR(SUM(mon_min) / 60), ':', LPAD(SUM(mon_min) % 60, 2, '0')),
        CONCAT(FLOOR(SUM(tue_min) / 60), ':', LPAD(SUM(tue_min) % 60, 2, '0')),
        CONCAT(FLOOR(SUM(wed_min) / 60), ':', LPAD(SUM(wed_min) % 60, 2, '0')),
        CONCAT(FLOOR(SUM(thu_min) / 60), ':', LPAD(SUM(thu_min) % 60, 2, '0')),
        CONCAT(FLOOR(SUM(fri_min) / 60), ':', LPAD(SUM(fri_min) % 60, 2, '0')),
        CONCAT(FLOOR(SUM(sat_min) / 60), ':', LPAD(SUM(sat_min) % 60, 2, '0')),
        CONCAT(FLOOR(SUM(sun_min) / 60), ':', LPAD(SUM(sun_min) % 60, 2, '0')),
        CONCAT(FLOOR(SUM(total_minutes) / 60), ':', LPAD(SUM(total_minutes) % 60, 2, '0')),
        CONCAT('$', FORMAT(AVG(CAST(REPLACE(REPLACE(rate, '$', ''), '/hr', '') AS DECIMAL(10,2))), 2), '/hr'),
        CONCAT('$', FORMAT(SUM((total_minutes / 60.0) * CAST(REPLACE(REPLACE(rate, '$', ''), '/hr', '') AS DECIMAL(10,2))), 2))
    FROM contract_summary
)
SELECT title, mon, tue, wed, thu, fri, sat, sun, hours, rate, amount
FROM final_result
ORDER BY id;

import inspect


def get_doc(fun: Callable) -> str:
    # write your code here
    sig = inspect.signature(fun)
    params = sig.parameters
    return_type = sig.return_annotation.__name__

    doc = "function name\n"
    doc += f"    {fun.__name__}\n"
    doc += f"params ({len(params)})\n"

    for param_name, param_obj in params.items():
        doc += f"    {param_name} {param_obj.annotation.__name__}\n"

    doc += "return type\n"
    doc += f"    {return_type}\n"

    int_counter = 2
    str_counter = ord('a')
    args_str = []
    args_actual = []

    for param_obj in params.values():
        if param_obj.annotation == int:
            args_str.append(str(int_counter))
            args_actual.append(int_counter)
            int_counter += 1
        else:
            s = chr(str_counter) * 3
            args_str.append(s)
            args_actual.append(s)
            str_counter += 1

    result = fun(*args_actual)

    doc += "example usage\n"
    doc += f"    {fun.__name__}({', '.join(args_str)}) -> {result}"

    return doc


def maxGameScore(cell):
    # Write your code here
    n = len(cell)
    dp = [float("-inf")] * n
    dp[0] = 0

    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    primes = [p for p in range(3, n, 10) if is_prime(p)]

    for i in range(n):
        if dp[i] == float("-inf"):
            continue
        if i + 1 < n:
            dp[i + 1] = max(dp[i + 1], dp[i] + cell[i + 1])
        for p in primes:
            if i + p < n:
                dp[i + p] = max(dp[i + p], dp[i] + cell[i + p])
    return dp[n - 1]
