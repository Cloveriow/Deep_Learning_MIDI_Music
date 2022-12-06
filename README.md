# deep-learning-MIDI-music
深度學習midi音樂，使用python的pytorch進行訓練
## 我做了什麼
https://github.com/WiraDKP/RNN_MIDI_Composer<br>
我很感謝WiraDKP的教學<br>
我自己編寫了轉換miditocsv和csvtomidi的code<br>
csvtomidi.py<br>
miditocsv.py<br>
並且修改了train.py,大幅降低了loss,並修復了他的bug,來自loss的資料型態錯誤,我不知道原因,他可能是由版本導致的?<br>

## 如何運行它
如同原版,你需要以下的函式庫<br>
- numpy
- pandas
- pytorch==0.4.1
- plac
- tqdm<br>
除此之外你還需要
- py_midicsv<br>
這是用來轉換midi和csv所需要的函式庫
## 如何製作需要的訓練集
我沒有把我的訓練集放上github,因為它們有版權的疑慮,所以你必須自行建立一個訓練資料。<br>
首先你需要擁有.midi的音樂檔案,接著點開miditocsv.py<br>
 ```name="is name"
csv_string = pm.midi_to_csv(name+".mid")
with open(name+"_out.csv", "w") as f:
    f.writelines(csv_string)
    
midi_object = pm.csv_to_midi(csv_string)

with open(name+"_out.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)
```
你只需要修改name讓它等於你要讀取的檔名按下編譯後變會轉換成csv<br>
## 訓練它
開啟train.py<br>
修改它的參數,或著使用我預設的參數執行,訓練完成的資料會放置於model資料夾<br>
除此之外我翻譯了說明的英文介紹<br>
## 作曲
使用Music Composer.ipynb筆記本,並選擇你要加載的模型,調整好參數,執行它<br>
接著便會產生出.csv檔<br>
## 將.csv檔轉換成.mid
我編寫了csvtomidi.py,它可以協助你轉換成.mid檔供您試聽
 ```
 import py_midicsv as pm

# Load the MIDI file and parse it into CSV format
name="mymusic11"

midi_object = pm.csv_to_midi(name+".csv")

# Save the parsed MIDI file to disk
with open(name+"_out.mid", "wb") as output_file:
    midi_writer = pm.FileWriter(output_file)
    midi_writer.write(midi_object)
 ```  
 同樣的你只需要修改讀取的檔案名稱,以及輸出的檔案名稱,變可以轉換成.mid<br>
 ## 試聽
 專案中的mymusic.csv以及mymusic4_out.mid等等是我的訓練成果,您可以下載下來試聽<br>
 或著您可以在這裡試聽,但是他需要會員<br>
 https://www.midishow.com/zh-tw/midi/161377.html<br>
 所以我在google drive也放了檔案<br>
 https://drive.google.com/drive/folders/1EZZ80QVb7_v4p8S9lH34LMTj63bFjjOr?usp=share_link<br>
 我推薦mymusic11_out.mid<br>
 它是我最後嘗試生產的mid檔案,它擁有最低的loss,並且相當動聽。<br>
 
 
