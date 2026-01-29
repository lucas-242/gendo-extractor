---
description: Create analytics functions and views
auto_execution_mode: 1
---

## Step 0 – Ensure docker is running

1. Check if docker is running
2. If not, prompt user to start docker

## Step 1 – Create functions

**FOREACH** file in `postgres/analytics/functions/*.sql` runs:

```bash
docker exec -i studio_postgres psql -U studio_user -d postgres < postgres/analytics/functions/{file}.sql    
```

## Step 2 – Create Views

**FOREACH** file in `postgres/analytics/views/*.sql` runs:

```bash
docker exec -i studio_postgres psql -U studio_user -d postgres < postgres/analytics/views/{file}.sql    
```