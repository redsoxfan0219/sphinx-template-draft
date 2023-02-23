# Markdown

## Data Dictionary

```{list-table} 
---
header-rows: 1
---
   * - Name
     - Age
   {% for key, value in names.iterrows() %}
   * - {{ value[0]}} {{value[1]}}
     - {{ value[2]}}
   {% endfor %}
``` 