```{list-table} 
   * - Name
     - Age
   {% for key, value in names.iterrows() %}
   * - {{ value[0]}} {{value[1]}}
     - {{ value[2]}}
   {% endfor %}

``` 