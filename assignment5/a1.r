seaflow <- read.csv(file="seaflow_21min.csv",head=TRUE,sep=",")
#summary(seaflow)

library(caret)
set.seed(3456)
trainIndex <- createDataPartition(seaflow$time, p = .5, list = FALSE, time = 1)
fileIdTrain <- seaflow$file_id[trainIndex]
timeTrain <- seaflow$time[trainIndex]
cellIdTrain <- seaflow$cell_id[trainIndex]
d1Train <- seaflow$d1[trainIndex]
d2Train <- seaflow$d2[trainIndex]
fscSmallTrain <- seaflow$fsc_small[trainIndex]
fscPerpTrain <- seaflow$fsc_perp[trainIndex]
fscBigTrain <- seaflow$fsc_big[trainIndex]
peTrain <- seaflow$pe[trainIndex]
chlSmallTrain <- seaflow$chl_small[trainIndex]
chlBigTrain <- seaflow$chl_big[trainIndex]
popTrain <- seaflow$pop[trainIndex]
seaflowTrain <- data.frame(file_id=fileIdTrain,
			   time=timeTrain,
			   cell_id=cellIdTrain,
			   d1=d1Train,
			   d2=d2Train,
			   fsc_small=fscSmallTrain,
			   fsc_perp=fscPerpTrain,
			   fsc_big=fscBigTrain,
		   	   pe=peTrain,
			   chl_small=chlSmallTrain,
			   chl_big=chlBigTrain,
			   pop=popTrain)
#summary(seaflowTrain)

#library(ggplot2)
#p <- ggplot(data = seaflow, aes(x = pe, y = chl_small, col = pop))
#p <- p + geom_point()
#p

library(rpart)

