install.packages("C50")
library(C50)
water_data = read.csv("C:\\Users\\Ali Fehmi Turan\\Desktop\\MACHINE_LEARNING_PART_CS59\\TRANSFORED_WATER_DATA_4.csv",na.strings=c("","NA"))
head(water_data,20)
#set.seed(9852) 
g <- runif(nrow(water_data)) 
water_r <- water_data[order(g), ] 
#water_r = water_data
water_r$classification<- as.factor(water_r$classification)
table(water_r$classification) 
summary(water_r)
dim(water_r)
dt <- C5.0(water_r[1:217, 1:4 ],water_r[1:217, 6 ] ) 
dt
summary(dt)
p1 <- predict(dt, water_r[218:317, -6]) 
table(water_r[218:317,6], Predicted = p1) 
plot(dt)

