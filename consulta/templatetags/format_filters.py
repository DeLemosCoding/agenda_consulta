from django import template

register = template.Library()


@register.filter
def format_cpf(value):
    value = str(value).replace(".", "").replace("-", "").strip()

    if len(value) != 11:
        return value

    return f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}"


@register.filter
def format_crm(value):
    value = str(value).replace(" ", "").replace("-", "").replace("/", "").strip()

    if len(value) < 3:
        return value

    uf = value[-2:].upper()
    numero = value[:-2]

    if len(numero) != 6:
        return value

    return f"{numero[:2]}-{numero[2:]}/{uf}"