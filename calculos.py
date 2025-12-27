def calcular_ir_plr(valor):
    if valor <= 7640.80:
        return 0.0
    elif valor <= 9922.28:
        return valor * 0.075 - 573.06
    elif valor <= 13167.00:
        return valor * 0.15 - 1316.68
    elif valor <= 16380.38:
        return valor * 0.225 - 2304.76
    else:
        return valor * 0.275 - 3123.78


def calcular_janeiro(salario, pl_salarios, ppr_salarios):
    valor_pl = salario * pl_salarios
    valor_ppr = salario * ppr_salarios

    bruto = valor_pl + valor_ppr
    ir = calcular_ir_plr(bruto)

    return {
        "bruto": bruto,
        "ir": ir,
        "liquido": bruto - ir,
        "pl": valor_pl,
        "ppr": valor_ppr
    }


def calcular_julho(salario, ppr_salarios, bruto_jan, ir_jan):
    valor_ppr = salario * ppr_salarios

    total_anual = bruto_jan + valor_ppr
    ir_total = calcular_ir_plr(total_anual)
    ir_julho = ir_total - ir_jan

    return {
        "bruto": valor_ppr,
        "ir": ir_julho,
        "liquido": valor_ppr - ir_julho
    }
