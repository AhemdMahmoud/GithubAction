with source as (
    select * from {{ ref('output_csv') }}
)

select
    id,
    name,
    age
from source