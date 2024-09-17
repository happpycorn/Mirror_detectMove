# 數位鏡面-遷

> 
> 寄蜉蝣於天地，渺滄海之一粟，哀吾生之須臾，羨長江之無窮。
>
> 挾飛仙以遨遊，抱眀月而長終。知不可乎驟得，託遺響於悲風。
>
> -前赤壁賦
> 

這是數位鏡面的第二個作品，起源於一個猜想：把兩張圖片互減是不是就可以看到他們的改變？

後來在學校中上了一門課叫做"數位設計"，最後的期末成果要策劃一個展覽，主題是"靠窗座位"。主題發想時不斷往下挖、尋找靠窗座位的本質，是窗外的景色嗎？是向前探索的期待嗎？我認為這個主題最重要的是"改變"。什麼是改變？兩個東西不一樣的地方就是改變。人是只看的到改變的，因為不變的東西太多太多了，許多痛苦的根源便像<前赤壁賦>中，只看見了改變、只看見失去，所以感覺什麼都沒留下。但是怎麼把這個表達出來？我想起了之前的猜想，將兩張照片互減，是不是就是改變？

## 實現方式

首先先來做做看兩張圖片互減會長怎樣吧，使用OpenCV來獲取影像，然後互減，再將結果用Pygame顯示出來，就這樣，第一版( [V0.0](/Code_version/V0.0.py) )做出來了。但做出來後，發現結果有點差強人意，他有點...不太直觀？看照片吧：

![image](Image/V0.0Image.gif)

他的視覺效果不是那麼的...好看？所以基於這個圖片，做了一些後來的處理後變成第二版( [V1.0](/Code_version/V1.0.py) )這樣：

![image](Image/V1.0Image.gif)

第二版做的最大改變有兩點：

+ **將畫面簡化成方塊增加運算速度，也更明顯。**
+ **加入了疊圖，我將前幾幀的畫面疊進來，並做淡化處理，讓整個變化呈現的更明顯。**

不過做出來後好像還差了點靠窗座位的感覺，所以又把他的淡化改成慢慢縮小的方塊，有點車子開遠的感覺，最終成品如下：

![image](Image/V2.0Image.gif)

補充：顯示用Pygame是一個繼承過來的小習慣，我會用的圖形介面有三個，OpenCV,Turtle,PyGame。習慣對應的是 Opencv：原影像、Turtle：控制介面、Pygame：處理過的影像，所以這邊就是多了一個步驟用Pygame檢視，而不是直接用OpenCV內建的顯示。

## 安裝方式

### 1.直接使用安裝包

到連結中下載打包好的.exe檔：[https://drive.google.com/file/d/1HUE9LsAZ99WnqsUZsaMwt_MIobXOjask/view?usp=drive_link](https://drive.google.com/file/d/1HUE9LsAZ99WnqsUZsaMwt_MIobXOjask/view?usp=drive_link)

下載下來後請 **確定電腦有接到任何一顆鏡頭**，然後開啟這個程式，順利的話就會看到畫面了。

### 2.使用原碼執行

在開始之前先確定你有安裝 Python3，如果沒有的話請先去 [Python官網](https://www.python.org/) 安裝。

確定有安裝 Python3 後，將"main.py"與"requirements.txt"下載下來，並在電腦上執行：
```
pip install -r requirements.txt
```
等待其下載完後**確定電腦有接到任何一顆鏡頭**，確定接到後執行：
```
python3 main.py
```
順利的話就會看到畫面了。

## 其他鏡子...

<a href="https://github.com/happpycorn/Mirror_Line">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=happpycorn&repo=Mirror_Line&theme=onedark&title_color=fff&icon_color=f9f9f9&text_color=9f9f9f&bg_color=151515" alt="Mirror_Line">
</a>
<a href="https://github.com/happpycorn/Mirror_mix">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=happpycorn&repo=Mirror_mix&theme=onedark&title_color=fff&icon_color=f9f9f9&text_color=9f9f9f&bg_color=151515" alt="Mirror_mix">
</a>
