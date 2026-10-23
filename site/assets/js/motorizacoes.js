/*
 * Motorizações por combustível, para o passo "Motorização" do formulário de avaliação.
 *
 * Para cada marca: "*" são as motorizações da marca (servem para qualquer modelo) e, nos modelos
 * mais vendidos, uma lista própria. A ordem de procura é: lista do modelo aqui → lista do modelo em
 * versoes.js (sem separação por combustível) → lista da marca ("*") → escolha genérica de cilindrada.
 * Combustíveis (iguais aos do passo "Combustível"): "Gasolina", "Gasóleo", "Híbrido",
 * "Híbrido plug-in", "Elétrico", "GPL / Bi-fuel". O cliente pode sempre escolher "Outra / não sei".
 * Os nomes da marca e do modelo têm de ser iguais aos de marcas.js.
 */
window.CC_MOTORES = {
  "Renault": {
    "*": {
      "Gasolina": ["0.9 TCe", "1.0 SCe", "1.0 TCe", "1.2 16v", "1.2 TCe", "1.3 TCe", "1.6 16v", "1.6 TCe", "1.8 TCe", "2.0 16v"],
      "Gasóleo": ["1.5 dCi", "1.5 Blue dCi", "1.6 dCi", "1.7 Blue dCi", "1.9 dCi", "2.0 dCi", "2.0 Blue dCi", "2.3 dCi"],
      "Híbrido": ["E-Tech full hybrid 145", "E-Tech full hybrid 160", "E-Tech full hybrid 200", "1.3 TCe mild hybrid"],
      "Híbrido plug-in": ["E-Tech plug-in 160"],
      "GPL / Bi-fuel": ["0.9 TCe GPL", "1.0 TCe GPL", "1.2 16v GPL"]
    },
    "Clio": {
      "Gasolina": ["1.2 16v 75 cv", "0.9 TCe 90 cv", "1.0 SCe 65/75 cv", "1.0 TCe 90/100 cv", "1.2 TCe 120 cv", "1.3 TCe 130/140 cv", "1.6 RS 200/220 cv"],
      "Gasóleo": ["1.5 dCi 75 cv", "1.5 dCi 90 cv", "1.5 dCi 110 cv", "1.5 Blue dCi 85 cv", "1.5 Blue dCi 100/115 cv"],
      "Híbrido": ["E-Tech hybrid 140/145 cv"],
      "GPL / Bi-fuel": ["0.9 TCe 90 GPL", "1.0 TCe 100 GPL"]
    },
    "Mégane": {
      "Gasolina": ["1.2 TCe 115/130 cv", "1.3 TCe 115/140/160 cv", "1.6 16v 110 cv", "1.8 TCe RS 280/300 cv", "2.0 RS 250/265/275 cv"],
      "Gasóleo": ["1.5 dCi 90/95/110 cv", "1.5 Blue dCi 95/115 cv", "1.6 dCi 130 cv", "1.7 Blue dCi 150 cv", "1.9 dCi 130 cv"],
      "Híbrido plug-in": ["E-Tech plug-in 160 cv"]
    },
    "Captur": {
      "Gasolina": ["0.9 TCe 90 cv", "1.0 TCe 90/100 cv", "1.2 TCe 120 cv", "1.3 TCe 130/140/150/155 cv"],
      "Gasóleo": ["1.5 dCi 90/110 cv", "1.5 Blue dCi 95/115 cv"],
      "Híbrido": ["E-Tech full hybrid 145 cv", "1.3 TCe mild hybrid 140/160 cv"],
      "Híbrido plug-in": ["E-Tech plug-in 160 cv"],
      "GPL / Bi-fuel": ["1.0 TCe 100 GPL"]
    }
  },
  "Dacia": {
    "*": {
      "Gasolina": ["1.0 SCe", "0.9 TCe", "1.0 TCe", "1.2 16v", "1.3 TCe", "1.6 SCe"],
      "Gasóleo": ["1.5 dCi", "1.5 Blue dCi"],
      "Híbrido": ["Hybrid 140", "Hybrid 155"],
      "GPL / Bi-fuel": ["1.0 ECO-G 100", "0.9 TCe GPL", "1.0 TCe GPL", "1.6 GPL"]
    }
  },
  "Peugeot": {
    "*": {
      "Gasolina": ["1.0 VTi", "1.2 VTi", "1.2 PureTech", "1.4 16v", "1.6 VTi", "1.6 THP", "1.6 PureTech"],
      "Gasóleo": ["1.4 HDi", "1.5 BlueHDi", "1.6 HDi", "1.6 BlueHDi", "2.0 HDi", "2.0 BlueHDi", "2.2 BlueHDi"],
      "Híbrido": ["Hybrid 136 (e-DCS6)", "Hybrid 145"],
      "Híbrido plug-in": ["Hybrid 180/195", "Hybrid 225", "Hybrid4 300"],
      "Elétrico": ["e-208 / e-2008 136 cv", "e-208 / e-2008 156 cv", "e-308 / e-3008 / e-5008"]
    },
    "208": {
      "Gasolina": ["1.0 VTi 68 cv", "1.2 VTi / PureTech 75/82 cv", "1.2 PureTech 100 cv", "1.2 PureTech 110 cv", "1.2 PureTech 130 cv", "1.6 THP GTi 200/208 cv"],
      "Gasóleo": ["1.4 HDi 68 cv", "1.6 HDi / BlueHDi 75/100/120 cv", "1.5 BlueHDi 100/102 cv"],
      "Híbrido": ["Hybrid 100", "Hybrid 136"],
      "Elétrico": ["e-208 136 cv", "e-208 156 cv"]
    },
    "308": {
      "Gasolina": ["1.2 PureTech 110 cv", "1.2 PureTech 130 cv", "1.6 VTi 120 cv", "1.6 THP 150/156 cv", "1.6 THP GTi 250/270 cv"],
      "Gasóleo": ["1.6 HDi 92/112 cv", "1.6 BlueHDi 100/120 cv", "1.5 BlueHDi 100/130 cv", "2.0 BlueHDi 150/180 cv"],
      "Híbrido": ["Hybrid 136", "Hybrid 145"],
      "Híbrido plug-in": ["Hybrid 180 cv", "Hybrid 225 cv"],
      "Elétrico": ["e-308 156 cv"]
    },
    "2008": {
      "Gasolina": ["1.2 VTi / PureTech 82 cv", "1.2 PureTech 100/110 cv", "1.2 PureTech 130 cv", "1.6 VTi 120 cv"],
      "Gasóleo": ["1.4 HDi 68 cv", "1.6 HDi / BlueHDi 92/100/120 cv", "1.5 BlueHDi 100/110/130 cv"],
      "Híbrido": ["Hybrid 136", "Hybrid 145"],
      "Elétrico": ["e-2008 136 cv", "e-2008 156 cv"]
    },
    "3008": {
      "Gasolina": ["1.2 PureTech 130 cv", "1.6 THP 150/165 cv", "1.6 PureTech 180 cv"],
      "Gasóleo": ["1.6 HDi 112/115 cv", "1.6 BlueHDi 120 cv", "1.5 BlueHDi 130 cv", "2.0 HDi / BlueHDi 150/163/180 cv"],
      "Híbrido": ["Hybrid 136", "Hybrid 145"],
      "Híbrido plug-in": ["Hybrid 225 cv", "Hybrid4 300 cv"],
      "Elétrico": ["e-3008"]
    }
  },
  "Citroën": {
    "*": {
      "Gasolina": ["1.0 VTi", "1.1i", "1.2 VTi", "1.2 PureTech", "1.4 16v", "1.6 VTi", "1.6 THP"],
      "Gasóleo": ["1.4 HDi", "1.5 BlueHDi", "1.6 HDi", "1.6 BlueHDi", "2.0 HDi", "2.0 BlueHDi"],
      "Híbrido": ["Hybrid 136", "Hybrid 145"],
      "Híbrido plug-in": ["Hybrid 180", "Hybrid 225"],
      "Elétrico": ["ë-C3", "ë-C4 136 cv", "ë-C4 156 cv"]
    },
    "C3": {
      "Gasolina": ["1.1i 60 cv", "1.0 VTi 68 cv", "1.2 VTi / PureTech 82/83 cv", "1.2 PureTech 110 cv", "1.4 16v 90/95 cv"],
      "Gasóleo": ["1.4 HDi 68/70 cv", "1.6 HDi / BlueHDi 75/92/100 cv", "1.5 BlueHDi 100/102 cv"],
      "Híbrido": ["Hybrid 100"],
      "Elétrico": ["ë-C3 113 cv"]
    }
  },
  "Opel": {
    "*": {
      "Gasolina": ["1.0", "1.2", "1.2 Turbo", "1.4", "1.4 Turbo", "1.6", "1.6 Turbo"],
      "Gasóleo": ["1.3 CDTI", "1.5 Diesel", "1.6 CDTI", "1.7 CDTI", "2.0 CDTI"],
      "Híbrido": ["Hybrid 100", "Hybrid 136 / 145"],
      "Híbrido plug-in": ["Hybrid 180", "Hybrid 225", "Hybrid4 300"],
      "Elétrico": ["Corsa Electric / e", "Mokka Electric / e", "Astra Electric"],
      "GPL / Bi-fuel": ["1.2 GPL", "1.4 GPL", "1.4 Turbo GPL"]
    },
    "Corsa": {
      "Gasolina": ["1.0 Turbo 90/115 cv", "1.2 60/70/75/80 cv", "1.2 Turbo 100 cv", "1.2 Turbo 130 cv", "1.4 90/100 cv", "1.6 Turbo OPC 150/192/207 cv"],
      "Gasóleo": ["1.3 CDTI 75/90/95 cv", "1.5 Diesel 100/102 cv", "1.7 CDTI 125/130 cv"],
      "Híbrido": ["Hybrid 100", "Hybrid 136"],
      "Elétrico": ["Corsa-e / Electric 136 cv", "Corsa Electric 156 cv"],
      "GPL / Bi-fuel": ["1.2 GPL", "1.4 GPL"]
    },
    "Astra": {
      "Gasolina": ["1.0 Turbo 105 cv", "1.2 Turbo 110/130/145 cv", "1.4 90/100 cv", "1.4 Turbo 125/140/150 cv", "1.6 115 cv", "1.6 Turbo 180/200 cv"],
      "Gasóleo": ["1.3 CDTI 90/95 cv", "1.5 Diesel 105/122/130 cv", "1.6 CDTI 110/136/160 cv", "1.7 CDTI 110/125/130 cv", "2.0 CDTI 160/165 cv"],
      "Híbrido plug-in": ["Hybrid 180 cv", "Hybrid 225 cv"],
      "Elétrico": ["Astra Electric 156 cv"]
    }
  },
  "Fiat": {
    "*": {
      "Gasolina": ["1.0 FireFly", "0.9 TwinAir", "1.1", "1.2", "1.4", "1.4 T-Jet", "1.4 MultiAir", "1.0 T3", "1.3 T4", "1.6 E-torQ"],
      "Gasóleo": ["1.3 Multijet", "1.6 Multijet", "1.9 Multijet", "2.0 Multijet", "2.3 Multijet"],
      "Híbrido": ["1.0 Hybrid", "1.2 Hybrid", "1.5 Hybrid"],
      "Elétrico": ["500e", "600e", "Grande Panda elétrico"],
      "GPL / Bi-fuel": ["1.2 GPL", "1.4 GPL", "0.9 TwinAir Natural Power (GNV)"]
    }
  },
  "Volkswagen": {
    "*": {
      "Gasolina": ["1.0 MPI", "1.0 TSI", "1.2 TSI", "1.4", "1.4 TSI", "1.5 TSI", "1.6", "1.6 FSI", "2.0 TSI", "2.0 TSI GTI", "2.0 TSI R"],
      "Gasóleo": ["1.2 TDI", "1.4 TDI", "1.6 TDI", "1.9 TDI", "2.0 TDI"],
      "Híbrido": ["1.0 eTSI", "1.5 eTSI"],
      "Híbrido plug-in": ["1.4 TSI eHybrid / GTE", "1.5 TSI eHybrid"],
      "Elétrico": ["e-up! / e-Golf", "ID. Pure / Standard", "ID. Pro", "ID. Pro S", "ID. GTX"],
      "GPL / Bi-fuel": ["1.0 TGI (GNV)", "1.4 TGI (GNV)", "1.5 TGI (GNV)"]
    },
    "Golf": {
      "Gasolina": ["1.0 TSI 110/115 cv", "1.2 TSI 85/105/110 cv", "1.4 80 cv", "1.4 TSI 122/125/140/150/160 cv", "1.5 TSI 130/150 cv", "1.6 102 cv", "2.0 TSI GTI 200-300 cv", "2.0 TSI R 270-333 cv"],
      "Gasóleo": ["1.6 TDI 90/105/110/115 cv", "1.9 TDI 90/105 cv", "2.0 TDI 115/140/150/170 cv", "2.0 TDI GTD 170-200 cv"],
      "Híbrido": ["1.0 eTSI 110 cv", "1.5 eTSI 130/150 cv"],
      "Híbrido plug-in": ["1.4 TSI GTE / eHybrid 204/245 cv", "1.5 eHybrid 204/272 cv"],
      "Elétrico": ["e-Golf 115/136 cv"]
    },
    "Polo": {
      "Gasolina": ["1.0 MPI 65/75/80 cv", "1.0 TSI 95/110 cv", "1.2 60/70 cv", "1.2 TSI 90/105 cv", "1.4 85 cv", "1.4 TSI GTI 180 cv", "2.0 TSI GTI 200/207 cv"],
      "Gasóleo": ["1.2 TDI 75 cv", "1.4 TDI 75/90 cv", "1.6 TDI 75/80/90/95/105 cv"],
      "GPL / Bi-fuel": ["1.0 TGI 90 cv (GNV)"]
    }
  },
  "Seat": {
    "*": {
      "Gasolina": ["1.0 MPI", "1.0 TSI", "1.2", "1.2 TSI", "1.4", "1.4 TSI", "1.5 TSI", "1.6", "2.0 TSI"],
      "Gasóleo": ["1.2 TDI", "1.4 TDI", "1.6 TDI", "1.9 TDI", "2.0 TDI"],
      "Híbrido": ["1.0 eTSI", "1.5 eTSI"],
      "Híbrido plug-in": ["1.4 e-Hybrid 204", "1.5 e-Hybrid"],
      "GPL / Bi-fuel": ["1.0 TGI (GNV)", "1.5 TGI (GNV)", "1.6 GPL"]
    },
    "Ibiza": {
      "Gasolina": ["1.0 MPI 75/80 cv", "1.0 TSI 95/110/115 cv", "1.2 60/70 cv", "1.2 TSI 90/105 cv", "1.4 85 cv", "1.5 TSI 150 cv", "1.4 TSI Cupra 150/180 cv"],
      "Gasóleo": ["1.2 TDI 75 cv", "1.4 TDI 75/80/90/105 cv", "1.6 TDI 80/90/95/105 cv", "1.9 TDI 100/130 cv"],
      "GPL / Bi-fuel": ["1.0 TGI 90 cv (GNV)"]
    },
    "Leon": {
      "Gasolina": ["1.0 TSI 110/115 cv", "1.2 TSI 105/110 cv", "1.4 TSI 122/125/140/150 cv", "1.5 TSI 130/150 cv", "1.6 102 cv", "2.0 TSI Cupra 240-300 cv"],
      "Gasóleo": ["1.6 TDI 90/105/110/115 cv", "1.9 TDI 105 cv", "2.0 TDI 140/150/170/184 cv"],
      "Híbrido": ["1.0 eTSI 110 cv", "1.5 eTSI 130/150 cv"],
      "Híbrido plug-in": ["1.4 e-Hybrid 204 cv", "1.5 e-Hybrid 204/272 cv"],
      "GPL / Bi-fuel": ["1.4 TGI (GNV)", "1.5 TGI (GNV)"]
    }
  },
  "Cupra": {
    "*": {
      "Gasolina": ["1.5 TSI 150 cv", "2.0 TSI 190 cv", "2.0 TSI 245 cv", "2.0 TSI 300/310 cv", "2.5 TSI VZ5 390 cv"],
      "Gasóleo": ["2.0 TDI 150 cv"],
      "Híbrido": ["1.5 eTSI 150 cv"],
      "Híbrido plug-in": ["1.4 e-Hybrid 204/245 cv", "1.5 e-Hybrid 204/272 cv"],
      "Elétrico": ["Born 204/231 cv", "Born VZ 326 cv", "Tavascan"]
    }
  },
  "Skoda": {
    "*": {
      "Gasolina": ["1.0 MPI", "1.0 TSI", "1.2", "1.2 TSI", "1.4", "1.4 TSI", "1.5 TSI", "2.0 TSI RS"],
      "Gasóleo": ["1.2 TDI", "1.4 TDI", "1.6 TDI", "1.9 TDI", "2.0 TDI"],
      "Híbrido": ["1.0 e-TEC", "1.5 e-TEC"],
      "Híbrido plug-in": ["1.4 TSI iV", "1.5 TSI iV"],
      "Elétrico": ["Enyaq / Elroq 50", "Enyaq / Elroq 60", "Enyaq / Elroq 80 / 85", "Enyaq RS"],
      "GPL / Bi-fuel": ["1.0 G-TEC (GNV)", "1.5 G-TEC (GNV)", "1.4 GPL"]
    }
  },
  "Audi": {
    "*": {
      "Gasolina": ["1.0 TFSI / 30 TFSI", "1.4 TFSI / 35 TFSI", "1.5 TFSI / 35 TFSI", "1.8 TFSI", "2.0 TFSI / 40-45 TFSI", "3.0 TFSI / 55 TFSI"],
      "Gasóleo": ["1.6 TDI / 30 TDI", "2.0 TDI / 35-40 TDI", "3.0 TDI / 45-50 TDI"],
      "Híbrido plug-in": ["40/45 TFSI e", "50/55 TFSI e quattro"],
      "Elétrico": ["e-tron / Q8 e-tron", "Q4 e-tron", "Q6 e-tron", "e-tron GT"]
    }
  },
  "Mercedes-Benz": {
    "*": {
      "Gasolina": ["160 / 180", "200", "250", "300", "350 / 400", "AMG 35 / 43", "AMG 45 / 53 / 63"],
      "Gasóleo": ["180 d / CDI", "200 d / CDI", "220 d / CDI", "250 d / CDI", "300 d / 350 d", "400 d"],
      "Híbrido plug-in": ["250 e", "300 e / de", "350 e / 400 e"],
      "Elétrico": ["EQA", "EQB", "EQC", "EQE", "EQS", "EQV / eVito"]
    }
  },
  "BMW": {
    "*": {
      "Gasolina": ["i 1.5 (3 cil.)", "i 2.0 (4 cil.)", "i 3.0 (6 cil.)", "M"],
      "Gasóleo": ["d 1.5 (3 cil.)", "d 2.0 (4 cil.)", "d 3.0 (6 cil.)"],
      "Híbrido plug-in": ["e / xe (plug-in)"],
      "Elétrico": ["i3 / i3s", "i4", "iX1 / iX2", "iX3", "iX", "i5 / i7"]
    }
  },
  "Mini": {
    "*": {
      "Gasolina": ["One 1.2/1.5 75-102 cv", "Cooper 1.5 136 cv", "Cooper S 2.0 178-192 cv", "John Cooper Works 2.0 231 cv"],
      "Gasóleo": ["One D 1.5 95 cv", "Cooper D 1.5/2.0 116-150 cv", "Cooper SD 2.0 170-190 cv"],
      "Híbrido plug-in": ["Cooper SE ALL4 (Countryman)"],
      "Elétrico": ["Cooper SE / E", "Cooper SE (2024)", "Aceman"]
    }
  },
  "Toyota": {
    "*": {
      "Gasolina": ["1.0 VVT-i", "1.33 / 1.4 VVT-i", "1.5 VVT-i", "1.6 VVT-i", "1.8 VVT-i", "2.0", "1.2 Turbo"],
      "Gasóleo": ["1.4 D-4D", "1.6 D-4D", "2.0 D-4D", "2.2 D-4D", "2.4 / 2.8 D-4D"],
      "Híbrido": ["1.5 Hybrid 100/116/130 cv", "1.8 Hybrid 122/136/140 cv", "2.0 Hybrid 184/196 cv", "2.5 Hybrid 218/222 cv"],
      "Híbrido plug-in": ["2.0 Plug-in Hybrid 223 cv", "2.5 Plug-in Hybrid 306 cv"],
      "Elétrico": ["bZ4X", "Urban Cruiser elétrico", "Proace elétrico"]
    },
    "Yaris": {
      "Gasolina": ["1.0 VVT-i 69/72 cv", "1.33 VVT-i 99/100 cv", "1.5 VVT-i 111/125 cv", "GR Yaris 1.6 Turbo 261/280 cv"],
      "Gasóleo": ["1.4 D-4D 90 cv"],
      "Híbrido": ["1.5 Hybrid 100 cv (até 2020)", "1.5 Hybrid 116 cv", "1.5 Hybrid 130 cv"]
    },
    "Corolla": {
      "Gasolina": ["1.2 Turbo 116 cv", "1.4 VVT-i 97 cv", "1.6 VVT-i 124/132 cv"],
      "Gasóleo": ["1.4 D-4D 90 cv", "2.0 D-4D 116/126 cv"],
      "Híbrido": ["1.8 Hybrid 122/140 cv", "2.0 Hybrid 184/196 cv"]
    },
    "C-HR": {
      "Gasolina": ["1.2 Turbo 116 cv"],
      "Híbrido": ["1.8 Hybrid 122/140 cv", "2.0 Hybrid 184/197 cv"],
      "Híbrido plug-in": ["2.0 Plug-in Hybrid 223 cv"]
    }
  },
  "Nissan": {
    "*": {
      "Gasolina": ["1.0 IG-T / DIG-T", "1.2 DIG-T", "1.3 DIG-T", "1.5 VC-T", "1.6", "1.2", "1.4"],
      "Gasóleo": ["1.5 dCi", "1.6 dCi", "1.7 dCi", "2.0 dCi", "2.3 dCi"],
      "Híbrido": ["1.3 DIG-T mild hybrid", "e-Power 190 cv", "1.6 Hybrid 143 cv"],
      "Elétrico": ["Leaf 24/30 kWh", "Leaf 40 kWh", "Leaf e+ 62 kWh", "Ariya", "Townstar elétrico"]
    },
    "Qashqai": {
      "Gasolina": ["1.2 DIG-T 115 cv", "1.3 DIG-T 140/160 cv", "1.6 117 cv", "1.6 DIG-T 163 cv", "2.0 141 cv"],
      "Gasóleo": ["1.5 dCi 106/110/115 cv", "1.6 dCi 130 cv", "1.7 dCi 150 cv", "2.0 dCi 150 cv"],
      "Híbrido": ["1.3 DIG-T mild hybrid 140/158 cv", "e-Power 190 cv"]
    }
  },
  "Ford": {
    "*": {
      "Gasolina": ["1.0 EcoBoost", "1.1 Ti-VCT", "1.25", "1.4", "1.5 EcoBoost", "1.6 Ti-VCT", "1.6 EcoBoost", "2.0 / 2.3 EcoBoost"],
      "Gasóleo": ["1.4 TDCi", "1.5 TDCi / EcoBlue", "1.6 TDCi", "1.8 TDCi", "2.0 TDCi / EcoBlue", "2.2 TDCi"],
      "Híbrido": ["1.0 EcoBoost mHEV", "2.5 FHEV"],
      "Híbrido plug-in": ["2.5 PHEV 225/243 cv"],
      "Elétrico": ["Mustang Mach-E", "Explorer elétrico", "E-Transit / E-Tourneo"]
    },
    "Fiesta": {
      "Gasolina": ["1.0 EcoBoost 100/125/140 cv", "1.1 Ti-VCT 70/75/85 cv", "1.25 60/82 cv", "1.4 96 cv", "1.5 EcoBoost ST 200 cv", "1.6 Ti-VCT 120 cv"],
      "Gasóleo": ["1.4 TDCi 68/70 cv", "1.5 TDCi 75/85/95 cv", "1.6 TDCi 90/95 cv"],
      "Híbrido": ["1.0 EcoBoost mHEV 125/155 cv"]
    },
    "Focus": {
      "Gasolina": ["1.0 EcoBoost 100/125 cv", "1.5 EcoBoost 150/182 cv", "1.6 Ti-VCT 85/105/125 cv", "2.3 EcoBoost ST/RS 280/350 cv"],
      "Gasóleo": ["1.5 TDCi / EcoBlue 95/115/120 cv", "1.6 TDCi 90/95/105/115 cv", "2.0 TDCi / EcoBlue 150/190 cv"],
      "Híbrido": ["1.0 EcoBoost mHEV 125/155 cv"]
    }
  },
  "Hyundai": {
    "*": {
      "Gasolina": ["1.0", "1.0 T-GDi", "1.1", "1.2", "1.25", "1.4", "1.6", "1.6 T-GDi", "2.0 T-GDi N"],
      "Gasóleo": ["1.1 CRDi", "1.4 CRDi", "1.6 CRDi", "1.7 CRDi", "2.0 CRDi", "2.2 CRDi"],
      "Híbrido": ["1.0 T-GDi 48V", "1.6 GDi Hybrid", "1.6 T-GDi Hybrid"],
      "Híbrido plug-in": ["1.6 GDi Plug-in", "1.6 T-GDi Plug-in"],
      "Elétrico": ["Kona elétrico 39/48 kWh", "Kona elétrico 64/65 kWh", "IONIQ elétrico", "IONIQ 5 / IONIQ 6", "Inster"],
      "GPL / Bi-fuel": ["1.0 GPL", "1.2 GPL"]
    }
  },
  "Kia": {
    "*": {
      "Gasolina": ["1.0", "1.0 T-GDi", "1.2", "1.25", "1.4", "1.6", "1.6 T-GDi"],
      "Gasóleo": ["1.1 CRDi", "1.4 CRDi", "1.6 CRDi", "1.7 CRDi", "2.0 CRDi", "2.2 CRDi"],
      "Híbrido": ["1.0 T-GDi 48V", "1.6 GDi Hybrid", "1.6 T-GDi Hybrid"],
      "Híbrido plug-in": ["1.6 GDi Plug-in", "1.6 T-GDi Plug-in"],
      "Elétrico": ["e-Niro / Niro EV 39 kWh", "e-Niro / Niro EV 64 kWh", "e-Soul", "EV3", "EV6", "EV9"],
      "GPL / Bi-fuel": ["1.0 GPL", "1.2 GPL"]
    }
  },
  "Volvo": {
    "*": {
      "Gasolina": ["T2 / T3", "T4 / T5", "T6", "B3 / B4 (mild hybrid)", "B5 / B6 (mild hybrid)"],
      "Gasóleo": ["D2", "D3", "D4", "D5", "B4 / B5 diesel (mild hybrid)"],
      "Híbrido plug-in": ["T5 Recharge", "T6 Recharge", "T8 Recharge"],
      "Elétrico": ["Single Motor", "Single Motor Extended Range", "Twin Motor"]
    }
  },
  "Tesla": {
    "*": {
      "Elétrico": ["Standard Range / RWD", "Long Range", "Performance", "Plaid"]
    }
  }
};
