from dataclasses import dataclass
from datetime import datetime
from typing import Optional

# {'busiId': 'ME', 'statId': 'ME174013', 'chgerId': '01', 'stat': '2', 
# 'statUpdDt': '20251114140523', 'lastTsdt': '20251114125002', 'lastTedt': '20251114133057', 'nowTsdt': ''}

@dataclass
class ChargerStatDto:
    busiId: Optional[str] = None
    statId: Optional[str] = None
    chgerId: Optional[str] = None
    stat: Optional[str] = None
    statUpdDt: Optional[str] = None
    lastTsdt: Optional[str] = None
    lastTedt: Optional[str] = None
    nowTsdt: Optional[str] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
