from calendar import month
from datetime import datetime, timezone
from dateutil.relativedelta import *
import pytz


def get_now():
    """Funcao para retornar a data e hora no fuso horario brasileiro

    Returns:
       NOW [int]: Retorna a data e hora no formato %Y%m%d%H%M%S
    """
    utc_dt = datetime.now(timezone.utc)
    BRT = pytz.timezone("Brazil/East")
    NOW = utc_dt.astimezone(BRT).strftime("%Y-%m-%d %H:%M:%S%Z:00")
    return NOW