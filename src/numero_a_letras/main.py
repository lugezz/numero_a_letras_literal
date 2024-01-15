MONEDA_SINGULAR = 'peso'
MONEDA_PLURAL = 'pesos'

DECIMAL_SINGULAR = 'centavo'
DECIMAL_PLURAL = 'centavos'

MAX_NUMERO = 999999999999

UNIDADES = (
    'cero',
    'uno',
    'dos',
    'tres',
    'cuatro',
    'cinco',
    'seis',
    'siete',
    'ocho',
    'nueve'
)

DIECIS = (
    'diez',
    'once',
    'doce',
    'trece',
    'catorce',
    'quince',
    'dieciseis',
    'diecisiete',
    'dieciocho',
    'diecinueve'
)

DECENAS = (
    'cero',
    'diez',
    'veinte',
    'treinta',
    'cuarenta',
    'cincuenta',
    'sesenta',
    'setenta',
    'ochenta',
    'noventa'
)

CIENTOS = (
    '_',
    'ciento',
    'doscientos',
    'trescientos',
    'cuatrocientos',
    'quinientos',
    'seiscientos',
    'setecientos',
    'ochocientos',
    'novecientos'
)


def numero_a_letras(numero: float) -> str:
    numero_entero = int(numero)
    if numero_entero > MAX_NUMERO:
        raise OverflowError('Número demasiado alto')
    if numero_entero < 0:
        return f'menos {numero_a_letras(abs(numero))}'
    letras_decimal = ''
    parte_decimal = int(round((abs(numero) - abs(numero_entero)) * 100))
    if parte_decimal > 0:
        letras_decimal = f'con {numero_a_letras(parte_decimal)}'
    if (numero_entero <= 99):
        resultado = leer_decenas(numero_entero)
    elif (numero_entero <= 999):
        resultado = leer_centenas(numero_entero)
    elif (numero_entero <= 999999):
        resultado = leer_miles(numero_entero)
    elif (numero_entero <= 999999999):
        resultado = leer_millones(numero_entero)
    else:
        resultado = leer_millardos(numero_entero)
    resultado = resultado.replace('uno mil', 'un mil')
    resultado = resultado.strip()
    resultado = resultado.replace(' _ ', ' ')
    resultado = resultado.replace('  ', ' ')
    if parte_decimal > 0:
        resultado = f'{resultado} {letras_decimal}'
    return resultado


def numero_a_moneda(numero):
    numero_entero = int(numero)
    parte_decimal = int(round((abs(numero) - abs(numero_entero)) * 100))
    centimos = ''
    if parte_decimal == 1:
        centimos = DECIMAL_SINGULAR
    else:
        centimos = DECIMAL_PLURAL
    moneda = ''
    if numero_entero == 1:
        moneda = MONEDA_SINGULAR
    else:
        moneda = MONEDA_PLURAL
    letras = numero_a_letras(numero_entero)
    letras = letras.replace('uno', 'un')
    letras_decimal = f'con {numero_a_letras(parte_decimal).replace("uno", "un")} {centimos}'
    letras = f'{letras} {moneda} {letras_decimal}'
    return letras


def leer_decenas(numero):
    if numero < 10:
        return UNIDADES[numero]
    decena, unidad = divmod(numero, 10)
    if unidad == 0:
        return DECENAS[decena]
    if numero <= 19:
        resultado = DIECIS[unidad]
    elif numero <= 29:
        resultado = f'veinti{UNIDADES[unidad]}'
    else:
        resultado = DECENAS[decena]
        if unidad > 0:
            resultado = f'{resultado} y {UNIDADES[unidad]}'
    return resultado


def leer_centenas(numero):
    centena, decena = divmod(numero, 100)

    if numero == 100:
        resultado = 'cien'
    else:
        resultado = CIENTOS[centena]
        if decena > 0:
            resultado = f'{resultado} {leer_decenas(decena)}'

    return resultado


def leer_miles(numero):
    millar, centena = divmod(numero, 1000)
    resultado = ''
    if (millar == 1):
        resultado = ''
    if (millar >= 2) and (millar <= 9):
        resultado = UNIDADES[millar]
    elif (millar >= 10) and (millar <= 99):
        resultado = leer_decenas(millar)
    elif (millar >= 100) and (millar <= 999):
        resultado = leer_centenas(millar)
    resultado = f'{resultado} mil'
    if centena > 0:
        resultado = f'{resultado} {leer_centenas(centena)}'
    return resultado


def leer_millones(numero):
    millon, millar = divmod(numero, 1000000)
    resultado = ''
    if (millon == 1):
        resultado = ' un millon '
    if (millon >= 2) and (millon <= 9):
        resultado = UNIDADES[millon]
    elif (millon >= 10) and (millon <= 99):
        resultado = leer_decenas(millon)
    elif (millon >= 100) and (millon <= 999):
        resultado = leer_centenas(millon)
    if millon > 1:
        resultado = f'{resultado} millones'
    if (millar > 0) and (millar <= 999):
        resultado = f'{resultado} {leer_centenas(millar)}'
    elif (millar >= 1000) and (millar <= 999999):
        resultado = f'{resultado} {leer_miles(millar)}'
    return resultado


def leer_millardos(numero):
    millardo, millon = divmod(numero, 1000000)
    return f'{leer_miles(millardo)} millones {leer_millones(millon)}'
