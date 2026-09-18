from django import template

register = template.Library()

@register.filter
def format_CRM(CRM):
    if not CRM:
        return ""

    CRM = str(CRM).strip()

    if len(CRM) == 7:
        return f"{CRM[:2]} {CRM[2:6]}-{CRM[6:]}/RJ"

    return CRM

@register.filter
def format_CPF(CPF):
    if not CPF:
        return ""

    CPF = str(CPF).strip()

    if len(CPF) == 11:
        return f"{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}"

    return CPF