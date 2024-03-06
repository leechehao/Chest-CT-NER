# Chest CT NER
識別 Chest CT 影像文字報告中的實體資訊，實體類別共 11 種，分別為：
+ Observation：影像上所觀察到的異狀。
+ Finding：臨床上的發現。
+ Diagnosis：放射科醫師所判斷的疾病。
+ Location：人體解剖位置資訊。
+ Certainty：否定詞。
+ Change：時間上的狀態變化。
+ Attribute：Observation 或 Finding 的描述資訊。
+ Size：尺寸大小資訊。
+ Treatment：手術治療等資訊。
+ Normal：正常現象的描述。
+ Date：時間資訊。

此儲存庫除了訓練模型之外，還按照 Continuous Training (CT) 流程的步驟進行模組化，因此會結合 Data Version Control (DVC) 和 Jenkins 的功能。

Continuous Training (CT) 流程的步驟：
+ Data extraction：當有新資料出現時，自動從多個來源提取數據。
+ Data validation：確保提取的數據符合預期的格式。
+ Data preparation：對數據進行預處理，包括清洗、轉換和特徵工程，以便模型可以有效地學習。
+ Model training：使用準備好的數據訓練模型。
+ Model evaluation：該模型在測試集上進行評估，以評估模型品質。
+ Model validation：該模型被確認足以進行部署－其預測性能優於某個基準。

## 訓練模型
訓練模型的程式碼是使用自己開發的 [haonlp](https://github.com/leechehao/HaoNLP.git) 套件，它主要結合了 PyTorch Lightning 和 Hydra 的強大功能。
