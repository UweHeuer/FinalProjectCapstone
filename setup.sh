#!/bin/bash
export DATABASE_URL="postgresql://capstone:capstone@uweheuer.spdns.de:5432/capstone"
export EXCITED="true"
export AUTH0_DOMAIN='uweheuer.eu.auth0.com'
export ALGORITHMS=['RS256']
export API_AUDIENCE='capstone'
export EP='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNoVm9pNTZ1N0FsTm5zQkJNRTEtMCJ9.eyJpc3MiOiJodHRwczovL3V3ZWhldWVyLmV1LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MjEwMzI4ZTJjNDhkYjAwNjg1YTE5ODAiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY0NTM0NDU2MiwiZXhwIjoxNjQ1NDMwOTYyLCJhenAiOiJHN2I4Z1puelNjMHJqTXhhRTJTV25FOHR4U2NBc3NNYSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.fd9mg2Z1XTQiYw6HS633cbvHdLJZzWOlYK4DdfWWsAB-hShW8E3rVgCZwg5Hy3tf3JPzWswCcjPgzZqoCwtKnr5HvJu9cownXThCRXr51mvYmjqW1FnM8WHx0zmjtks1LkvRfMjumgipZ-Usrhg88Db53-WEabx1QMYT0EiWb7VCQTzELH17ydtHe9eNqHgOjE8IIYfi8P1Z92ienOn6z3BgkNCokR5J0Ppzy6Fqrg1dowqnHX3EnQZqoeS7tB1HHeTgkgKBl6wo2wJ5GpvxOfFHL9SQNJK18aSvEO6hg1Z1d0FVZrUBZ4dMTDKmyHcguG8zm7aLnzf0gzmoVColDQ'
echo "setup.sh script executed successfully!"