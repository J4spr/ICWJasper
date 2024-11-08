class JasperHeeftEenProbleem(Exception):
    pass


try:
    raise JasperHeeftEenProbleem
except JasperHeeftEenProbleem:
    pass


class JasperHeeftNogEenProbleem(Exception):
    pass


try:
    raise JasperHeeftNogEenProbleem
except JasperHeeftNogEenProbleem:
    pass


class TeGrootNummer(Exception):
    pass


try:
    raise TeGrootNummer
except:
    pass
