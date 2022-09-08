library(tseries)
library(astsa)
library(imputeTS)
library(forecast)
library(magrittr)
library(dplyr)
library(lubridate)
library(tidyr)

#
# Demo 1: Time series on snow in Sörenberg
#
setwd('C:/Users/salomon/switchdrive/HSLU/Nachhaltigkeit/Daten/Idaweb/')

#
# Snow in Sörenberg - daily series
# Ex: Record challenges of this procedure with real data - we'll address them all
#
slfso=read.csv('Sörenberg-TS.csv', header=TRUE, sep=';', na.strings='-')
colnames(slfso) <- c('Date', 'fresh_snow', 'total_snow')

slfso$Date <- as.Date(format(slfso$Date), '%Y%m%d')

# Fill time gaps and replace NA by 0
slfso %<>% complete(Date=seq.Date(min(Date), max(Date), by='day'))

# Use the time series class of the library stats
freq_daily <- 365.2422
fresh_snow <-
  ts(slfso$fresh_snow, start=c(year(min(slfso$Date)),yday(min(slfso$Date))), frequency=freq_daily) %>%
  na_replace(fill=0)
total_snow <-
  ts(slfso$total_snow, start=c(year(min(slfso$Date)), yday(min(slfso$Date))), frequency=freq_daily) %>%
  na_replace(fill=0)
plot(fresh_snow)

# Stationarity test and decomposition
adf.test(fresh_snow,k=0)
adf.test(total_snow,k=0)
fresh_snow_comp=decompose(fresh_snow)
total_snow_comp=decompose(total_snow)
plot(fresh_snow_comp)

# Manual decomposition
slfso %<>% mutate(year=year(slfso$Date)+yday(slfso$Date)/freq_daily)
fresh_snow_trend <- lm(slfso$fresh_snow~slfso$year)
plot(fresh_snow)
abline(fresh_snow_trend)

# Ex:How would you continue? - Write down the formula

#
# Temperature and precipitation in Flühli (hypothesis: Temperature has an influcene)
#
# Similar procedure as above
flu2=read.csv('Flühli-TS.csv', header=TRUE, sep=';', na.strings='-')
colnames(flu2)
colnames(flu2)[c(1,4)] <- c('Date','temp')
flu2$Date <- as.Date(format(flu2$Date), '%Y%m%d')
flu2 %<>% complete(Date=seq.Date(min(Date), max(Date), by='day'))
stdt <- as.Date('20.03.2015', '%d.%m.%Y')
temp_ts <- ts(filter(flu2, Date>=stdt)$temp, start=c(year(stdt), yday(stdt)), frequency=freq_daily) %>%
  na_replace(fill=0)
plot(temp_ts)
plot(total_snow)
temp_comp=decompose(temp_ts)
plot(temp_comp)

acf(temp_comp$random,na.action=na.pass)
pacf(temp_comp$random,na.action=na.pass)
pacf(temp_ts)

# Compare graphically
plot(temp_comp$random)
plot(fresh_snow_comp$random)

# Compare mathematically
window <- list(start=2016,end=2021)

# Make the time series comparable
temp_comp_random <- data.frame(Date=time(temp_comp$random), Random=temp_comp$random)
fresh_snow_comp_random <- data.frame(Date=time(fresh_snow_comp$random), Random=fresh_snow_comp$random)
#
temp_comp_random %<>% filter(Date>=window$start&Date<window$end)
fresh_snow_comp_random %<>% filter(Date>=window$start&Date<window$end)
#
temp_comp_random_ts <- ts(temp_comp_random$Random, start=c(window$start,1), frequency=freq_daily)
fresh_snow_comp_random_ts <- ts(fresh_snow_comp_random$Random, start=c(window$start,1), frequency=freq_daily)

# Cross correlation function
ccf(temp_comp_random_ts,fresh_snow_comp_random_ts)

# Ex: What do you find with the total snow height?

# Autocorrelation and ARIMA model
arima(temp_comp_random_ts, c(2,0,0))
sd(temp_comp_random_ts)
plot(ts(arima.sim(n=round((window$end-window$start)*freq_daily),model=list(ar=c(0.89,-0.18), ma=c(), sd=3.4)), start=c(window$start,1), frequency=freq_daily))
plot(temp_comp_random_ts)

# Ex: Which conclusions do you take from this?

#
# Yearly and monthly data are already prepared
#
slfso_yr <- slfso %>%
  mutate(fresh_snow_raw=replace_na(fresh_snow,0), total_snow_raw=replace_na(total_snow,0)) %>%
  group_by(Year=year(Date)) %>%
  summarize(fresh_snow=sum(fresh_snow_raw), total_snow=mean(total_snow_raw),
            fresh_snow_days=sum(as.integer(fresh_snow_raw>0)), total_snow_days=sum(as.integer(total_snow_raw>0))) %>%
  ungroup()
slfso_mn <- slfso %>%
  mutate(fresh_snow_raw=replace_na(fresh_snow,0), total_snow_raw=replace_na(total_snow,0)) %>%
  mutate(Year=year(Date), Month=month(Date)) %>%
  group_by(Year, Month) %>%
  summarize(fresh_snow=sum(fresh_snow_raw), total_snow=mean(total_snow_raw),
            fresh_snow_days=sum(as.integer(fresh_snow_raw>0)), total_snow_days=sum(as.integer(total_snow_raw>0)),
            .groups='keep') %>%
  ungroup()
temp_yr <- flu2 %>%
  mutate(temp_raw=replace_na(temp,0)) %>%
  group_by(Year=year(Date)) %>%
  filter(Year>=2016 & Year<=2021) %>%
  summarize(temp_yr=mean(temp_raw)) %>%
  ungroup()
temp_mn <- flu2 %>%
  mutate(temp_raw=replace_na(temp,0)) %>%
  group_by(Year=year(Date), Month=month(Date)) %>%
  filter(Year>=2016 & Year<=2021) %>%
  summarize(temp_mn=mean(temp_raw), .groups='keep') %>%
  ungroup()

# Time series
fresh_snow_yr <- ts(slfso_yr$fresh_snow, start=min(slfso_yr$Year), frequency=1)
total_snow_yr <- ts(slfso_yr$total_snow, start=min(slfso_yr$Year), frequency=1)
temp_snow_yr <- ts(temp_yr$temp_yr, start=min(temp_yr$Year), frequency=1)
fresh_snow_mn <- ts(slfso_mn$fresh_snow, start=c(slfso_mn$Year[1],slfso_mn$Month[1]), frequency=12)
total_snow_mn <- ts(slfso_mn$total_snow, start=c(slfso_mn$Year[1],slfso_mn$Month[1]), frequency=12)
temp_snow_mn <- ts(temp_mn$temp_mn, start=c(temp_mn$Year[1],temp_mn$Month[1]), frequency=12)

# Manual decomposition
fresh_snow_trend <- lm(slfso_yr$fresh_snow~slfso_yr$Year)
plot(fresh_snow_yr, xlab='Year', ylab='Average snow height [cm]')
abline(fresh_snow_trend)
lines(slfso_yr$Year, fresh_snow_trend$residuals, col='blue')
fresh_snow_yr_res <- ts(fresh_snow_trend$residuals, start=min(slfso_yr$Year), frequency=1)

# Why are they "equally stationary"?
adf.test(fresh_snow_yr,k=20)
adf.test(fresh_snow_yr_res,k=20)

# Here's the solution...
plot(fresh_snow_yr, ylim=c(-400,800))
lines(fresh_snow_yr_res,col='blue')

# Ex: Keep exploring - what do the results mean - why does the library refuse to decompose the yearly?
plot(total_snow_yr)
pacf(total_snow_yr)
pacf(total_snow_mn)
plot(total_snow_mn)
plot(tbats(total_snow_yr)) # Why not decompose()?
plot(residuals(tbats(total_snow_yr)))
plot(decompose(total_snow_mn)) # Compare to TBATS model
adf.test(total_snow_mn)

#
# Ex: Explore temperature and precipitation, homogenized, Luzern
#

#
# Demo 2: Stochastic process "bootstrap"
#
# Stochastic process 1: AR(2)
ts1 <- ts(arima.sim(n=80,model=list(ar=c(0.49,-0.5), ma=c(), sd=1)), start=c(2020,1), frequency=4)

plot(ts1)

# Stochastic process 2: AR(2)
# White noise process
w <- rnorm(80, mean=0, sd=1)
# Pulse response
w <- c(1, rep(0,79))
# AR parameters
ar <- c(0,1)
# Simulation
t <- c(w[1],w[2]+ar[1]*w[1])
for (i in 3:80) {
  t <- c(t,w[i]+t[i-1]*ar[1]+t[i-2]*ar[2])
}
ts2 <- ts(t, start=c(2020,1), frequency=4)

# Test the simulated time series and determine the stochastic process
adf.test(ts1,k=2)
acf(ts1)
pacf(ts1)
a=arima(ts1, c(2,0,0))

# Stochastic process 3: Poisson
Poisson <- function(k,l){return(l^k*exp(-l)/factorial(k))}
Poisson(1,2)
dpois(1,2)
rpois(20,0.05)

# Homogeneous / non-homogeneous
h <- rpois(1000,10)
mean(h)
var(h)
m <- 1+0.5*sin(2*pi*1:1000/1000)
nh <- rpois(1000,10*m)
mean(nh)
var(nh)

# Binomial and negative binomial
b <- rbinom(1000,100,0.1)
mean(b)
var(b)
nb <- rnbinom(1000,12,mu=10)
mean(nb)
var(nb)
