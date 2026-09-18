from django import template

register = template.Library()


@register.filter
def format_crm(crm):
    if not crm:
        return ""

    crm = str(crm).strip()

    if len(crm) == 7:
        return f"{crm[:2]} {crm[2:6]}-{crm[6:]}/RJ"

    return crm


@register.filter
def format_cpf(cpf):
    if not cpf:
        return ""

    cpf = str(cpf).strip()

    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    return cpf