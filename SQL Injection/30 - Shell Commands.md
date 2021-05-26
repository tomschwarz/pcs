# Execute shell commands

## MySQL
```sql
# Example usage
SELECT trim(trailing char(0x00) from exec_cmd("echo 'Hello World'"));

# Decode base64 string and write to file
SELECT trim(trailing char(0x00) from exec_cmd("echo 'SGVsbG8gV29ybGQK' | base64 -d >> /tmp/test.txt"));
```