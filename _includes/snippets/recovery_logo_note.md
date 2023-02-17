{%- if is_pe_recovery == true %}
{%- capture content %}
If your recovery does **not** show the PixelExperience logo, you accidentally booted into the wrong recovery. Please start at the top of this section!
{%- endcapture %}
    {% include alerts/note.html content=content %}
{%- endif -%}