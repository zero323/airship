{% for file in files %}
## {{ file.name }}
{% for paragraph in file.paragraphs %}
{% if paragraph.text and not paragraph.text.startswith("%md") %}
```scala
{{ paragraph.text | safe }}
```
{% if paragraph.msg %}
```
{{ paragraph.msg  | safe }}
```
{% endif %}
{% else %}
{{ paragraph.text }}
{% endif %}


{% endfor %}
{% endfor %}
