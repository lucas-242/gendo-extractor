---
description: Create database and tables
auto_execution_mode: 1
---

## Step 0 – Ensure docker is running

1. Check if docker is running
2. If not, prompt user to start docker

## Step 1 – Create database

1. Create database `studio`

```bash
docker exec -i studio_postgres psql -U studio_user -d postgres < postgres/init/001_create_database.sql    
```

2. Create schemas
```bash
docker exec -i studio_postgres psql -U studio_user -d studio < postgres/init/002_create_schemas.sql    
```

3. Create table `raw.gendo_report_304`
```bash
docker exec -i studio_postgres psql -U studio_user -d studio < postgres/init/003_create_raw_gendo_report_304.sql    
```