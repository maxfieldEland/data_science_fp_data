library(mfp)
library(xtable)
library(rms)
library(AIC)
library(MASS)
require(foreign)
require(nnet)
library(nlme)
model_features <- read.csv("C:/Users/mgreen13/Desktop/Desktop/spring19/ds_2/model_features.csv")

# manova test

m1 <- manova(cbind(dist,diff,depth,factor(hold))~factor(qual), data=model_features)

names(summary(m1))
summary(m1, test="Wilks")$stats
summary(m1, test="Wilks")


###Since we rejected H0, we want to find which groups are different and how they are different

#Start by doing F-tests for each variable


#Using the functions in R
m11 <- aov(dist~as.factor(qual),data=model_features)
summary(m11)
xtable(m11)

m12 <- aov(diff~as.factor(qual),data=model_features)
summary(m12)
confint(m12)

m13 <- aov(depth~as.factor(qual),data=model_features)
summary(m13)

###CKG_LOSS, MOIST, and HEX all have differences across groups.
#Lets examine to see which groups are different across the variable MOIST
(critval <- qt(.975,N-k))
(SE <- sqrt((1/5+1/5)*E[3,3]/(N-k)))

diffmat <- matrix(0,nrow=5,ncol=5) 
row.names(diffmat) <- row.names(meanvec)
colnames(diffmat) <- row.names(meanvec) 
for (i in 1:k){
  for (j in 1:k){
    diffmat[i,j] <- abs((meanvec[i,3]-meanvec[j,3])/SE)
  }#end j
}#end i
diffmat>critval


sub <- data.frame(model_features[sample(nrow(model_features),23000),])
# dichotomise variables
sub$qual_d <- factor(ifelse(sub$qual == 3,1,0))
sub$hold_d <- factor(ifelse(sub$hold ==4,1,0))

full_model <- glm(qual ~ diff+depth+hold_d+dist, data = sub, family = 'binomial')
summary(full_model)
xtable(full_model)
exp(0.1628)
exp(full_model$coefficients)
# check for potential non linearity

f10 = mfp(qual ~ fp(depth) + fp(dist) +hold + diff ,family = 'binomial',data=sub,verbose = TRUE)
sub$depth_t = (sub$depth)^(-0.5)
trans_model <-glm(qual ~ log(dist) +depth_t + hold_d + diff,family = 'binomial',data = sub)
summary(trans_model)
xtable(trans_model)

AIC(full_model,trans_model)
exp(coef(trans_model))

# multinom

# specify 0 as baseline outcome
mn <- polr(as.factor(qual) ~ diff+depth+hold_d+dist, data = unclass(sub), Hess = TRUE)
summary(mn)
exp(coef(mn))
