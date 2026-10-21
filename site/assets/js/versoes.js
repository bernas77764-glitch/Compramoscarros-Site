/*
 * Versões (motorizações) por marca e modelo, para o passo "Versão" do formulário de avaliação.
 *
 * O passo só aparece nos modelos que estão nesta lista; nos outros é saltado. O cliente pode
 * sempre escolher "Outra / não sei". Para acrescentar uma marca, um modelo ou uma versão, basta
 * editar esta lista (os nomes da marca e do modelo têm de ser iguais aos de marcas.js).
 */
window.CC_VERSOES = {
  "BMW": {
    "Série 1": ["116i", "118i", "120i", "125i", "128ti", "M135i", "116d", "118d", "120d", "123d", "125d"],
    "Série 2": ["218i", "220i", "230i", "M235i", "M240i", "218d", "220d", "225d"],
    "Série 2 Active Tourer": ["216i", "218i", "220i", "223i", "225xe", "230e", "216d", "218d", "220d"],
    "Série 2 Gran Coupé": ["216i", "218i", "220i", "M235i", "216d", "218d", "220d"],
    "Série 2 Gran Tourer": ["216i", "218i", "220i", "216d", "218d", "220d"],
    "Série 3": ["316i", "318i", "320i", "328i", "330i", "335i", "340i", "M340i", "330e", "316d", "318d", "320d", "325d", "330d", "335d", "M340d"],
    "Série 4": ["418i", "420i", "428i", "430i", "435i", "440i", "M440i", "418d", "420d", "425d", "430d", "435d"],
    "Série 5": ["520i", "523i", "525i", "528i", "530i", "535i", "540i", "550i", "M550i", "530e", "545e", "518d", "520d", "525d", "530d", "535d", "540d", "M550d"],
    "Série 6": ["630i", "640i", "650i", "620d", "630d", "640d"],
    "Série 7": ["730i", "740i", "750i", "760i", "740e", "745e", "730d", "740d", "750d"],
    "Série 8": ["840i", "M850i", "840d"],
    "X1": ["sDrive18i", "sDrive20i", "xDrive23i", "xDrive25e", "xDrive30e", "sDrive16d", "sDrive18d", "xDrive18d", "sDrive20d", "xDrive20d"],
    "X2": ["sDrive18i", "sDrive20i", "M35i", "xDrive25e", "sDrive18d", "xDrive20d"],
    "X3": ["xDrive20i", "xDrive30i", "M40i", "xDrive30e", "sDrive18d", "xDrive20d", "xDrive30d", "M40d"],
    "X4": ["xDrive20i", "xDrive30i", "M40i", "xDrive20d", "xDrive30d", "M40d"],
    "X5": ["xDrive40i", "xDrive45e", "xDrive50e", "M50i", "M60i", "xDrive25d", "xDrive30d", "xDrive40d", "M50d"],
    "X6": ["xDrive40i", "M50i", "M60i", "xDrive30d", "xDrive40d", "M50d"],
    "X7": ["xDrive40i", "M50i", "M60i", "xDrive30d", "xDrive40d", "M50d"],
    "Z4": ["sDrive20i", "sDrive30i", "M40i"],
    "i4": ["eDrive35", "eDrive40", "xDrive40", "M50"],
    "iX": ["xDrive40", "xDrive45", "xDrive50", "xDrive60", "M60"],
    "iX1": ["eDrive20", "xDrive30"]
  },
  "Mercedes-Benz": {
    "Classe A": ["A 160", "A 180", "A 200", "A 220", "A 250", "A 250 e", "A 35 AMG", "A 45 AMG", "A 160 d", "A 180 d", "A 200 d", "A 220 d"],
    "Classe B": ["B 160", "B 180", "B 200", "B 220", "B 250", "B 250 e", "B 180 d", "B 200 d", "B 220 d"],
    "Classe C": ["C 160", "C 180", "C 200", "C 250", "C 300", "C 300 e", "C 350 e", "C 43 AMG", "C 63 AMG", "C 200 d", "C 220 d", "C 250 d", "C 300 d"],
    "Classe E": ["E 200", "E 250", "E 300", "E 300 e", "E 350", "E 400", "E 450", "E 53 AMG", "E 200 d", "E 220 d", "E 250 d", "E 300 de", "E 350 d", "E 400 d"],
    "Classe CLA": ["CLA 180", "CLA 200", "CLA 220", "CLA 250", "CLA 250 e", "CLA 35 AMG", "CLA 45 AMG", "CLA 180 d", "CLA 200 d", "CLA 220 d"],
    "Classe CLK": ["CLK 200", "CLK 230", "CLK 320", "CLK 270 CDI"],
    "Classe CLS": ["CLS 350", "CLS 400", "CLS 450", "CLS 53 AMG", "CLS 220 d", "CLS 300 d", "CLS 350 d", "CLS 400 d"],
    "Classe GLA": ["GLA 180", "GLA 200", "GLA 220", "GLA 250", "GLA 250 e", "GLA 35 AMG", "GLA 45 AMG", "GLA 180 d", "GLA 200 d", "GLA 220 d"],
    "Classe GLB": ["GLB 180", "GLB 200", "GLB 220", "GLB 250", "GLB 35 AMG", "GLB 180 d", "GLB 200 d", "GLB 220 d"],
    "Classe GLC": ["GLC 200", "GLC 250", "GLC 300", "GLC 300 e", "GLC 350 e", "GLC 43 AMG", "GLC 63 AMG", "GLC 200 d", "GLC 220 d", "GLC 250 d", "GLC 300 d", "GLC 300 de"],
    "Classe GLE": ["GLE 350", "GLE 450", "GLE 53 AMG", "GLE 63 AMG", "GLE 300 d", "GLE 350 d", "GLE 350 de", "GLE 400 d"],
    "Classe GLK": ["GLK 200 CDI", "GLK 220 CDI", "GLK 250 CDI", "GLK 350 CDI"],
    "Classe GLS": ["GLS 450", "GLS 580", "GLS 63 AMG", "GLS 350 d", "GLS 400 d"],
    "Classe M": ["ML 250 BlueTEC", "ML 270 CDI", "ML 320 CDI", "ML 350 BlueTEC"],
    "Classe S": ["S 350", "S 400", "S 450", "S 500", "S 580", "S 580 e", "S 350 d", "S 400 d"],
    "Classe SL": ["SL 350", "SL 400", "SL 500", "SL 43 AMG", "SL 55 AMG", "SL 63 AMG"],
    "Classe SLK / SLC": ["SLK 200", "SLK 250", "SLK 350", "SLC 180", "SLC 200", "SLC 300", "SLK 250 d"],
    "Classe V": ["V 200 d", "V 220 d", "V 250 d", "V 300 d"],
    "Citan": ["108 CDI", "109 CDI", "111 CDI", "112"],
    "Vito": ["109 CDI", "111 CDI", "114 CDI", "116 CDI", "119 CDI"],
    "Sprinter": ["211 CDI", "213 CDI", "311 CDI", "313 CDI", "314 CDI", "316 CDI", "319 CDI"],
    "EQA": ["EQA 250", "EQA 250+", "EQA 300 4MATIC", "EQA 350 4MATIC"],
    "EQB": ["EQB 250", "EQB 300 4MATIC", "EQB 350 4MATIC"],
    "EQE": ["EQE 300", "EQE 350+", "EQE 500 4MATIC"],
    "EQS": ["EQS 450+", "EQS 580 4MATIC"]
  },
  "Audi": {
    "A1": ["25 TFSI", "30 TFSI", "35 TFSI", "40 TFSI", "1.0 TFSI", "1.4 TFSI", "1.6 TDI"],
    "A3": ["30 TFSI", "35 TFSI", "40 TFSI e", "45 TFSI e", "1.0 TFSI", "1.4 TFSI", "1.5 TFSI", "30 TDI", "35 TDI", "40 TDI", "1.6 TDI", "2.0 TDI"],
    "A4": ["35 TFSI", "40 TFSI", "45 TFSI", "30 TDI", "35 TDI", "40 TDI", "45 TDI", "2.0 TDI", "3.0 TDI"],
    "A5": ["35 TFSI", "40 TFSI", "45 TFSI", "35 TDI", "40 TDI", "45 TDI", "50 TDI", "2.0 TDI"],
    "A6": ["40 TFSI", "45 TFSI", "55 TFSI", "50 TFSI e", "55 TFSI e", "35 TDI", "40 TDI", "45 TDI", "50 TDI", "2.0 TDI", "3.0 TDI"],
    "A7": ["45 TFSI", "55 TFSI", "50 TFSI e", "55 TFSI e", "40 TDI", "45 TDI", "50 TDI"],
    "A8": ["55 TFSI", "60 TFSI e", "50 TDI"],
    "Q2": ["30 TFSI", "35 TFSI", "30 TDI", "35 TDI"],
    "Q3": ["35 TFSI", "40 TFSI", "45 TFSI", "45 TFSI e", "35 TDI", "40 TDI"],
    "Q4 e-tron": ["35 e-tron", "40 e-tron", "45 e-tron", "50 e-tron quattro"],
    "Q5": ["40 TFSI", "45 TFSI", "50 TFSI e", "55 TFSI e", "35 TDI", "40 TDI", "50 TDI"],
    "Q7": ["45 TFSI", "55 TFSI", "55 TFSI e", "60 TFSI e", "45 TDI", "50 TDI"],
    "Q8": ["55 TFSI", "60 TFSI e", "45 TDI", "50 TDI"],
    "e-tron": ["50 quattro", "55 quattro", "S"],
    "TT": ["40 TFSI", "45 TFSI", "TTS", "2.0 TDI"]
  },
  "Volvo": {
    "V40": ["T2", "T3", "T4", "T5", "D2", "D3", "D4"],
    "V60": ["B3", "B4", "T4", "T5", "T6 Recharge", "T8 Recharge", "D3", "D4"],
    "V90": ["B4", "B5", "T5", "T8 Recharge", "D3", "D4", "D5"],
    "S60": ["B4", "B5", "T4", "T5", "T8 Recharge", "D3", "D4"],
    "S90": ["B5", "T8 Recharge", "D4", "D5"],
    "XC40": ["T2", "T3", "T4", "B3", "B4", "T4 Recharge", "T5 Recharge", "D3", "D4", "Recharge (elétrico)"],
    "XC60": ["B4 gasolina", "B4 diesel", "B5", "T5", "T6 Recharge", "T8 Recharge", "D3", "D4", "D5"],
    "XC90": ["B5", "B6", "T5", "T6", "T8 Recharge", "D4", "D5"],
    "C40": ["Recharge Single Motor", "Recharge Twin Motor"],
    "EX30": ["Single Motor", "Single Motor Extended Range", "Twin Motor Performance"]
  }
};
