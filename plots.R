library(plotly)

df <- read.csv(file="temer_emotions.csv",head=TRUE)
df$index <- as.numeric(row.names(df))
df$seconds <- seq(1, 307, length.out=8595)

# ======= Smoothing method: gam ===========
ggplot(df, aes(seconds)) +
  geom_smooth(aes(y = anger, colour = "anger")) +
  geom_smooth(aes(y = contempt, colour = "contempt")) +
  geom_smooth(aes(y = disgust, colour = "disgust")) +
  geom_smooth(aes(y = fear, colour = "fear")) +
  geom_smooth(aes(y = happiness, colour = "happiness")) +
  geom_smooth(aes(y = sadness, colour = "sadness")) +
  geom_smooth(aes(y = surprise, colour = "surprise")) +
  scale_color_manual(values=c(anger="#FF3333",contempt="#C20084",disgust="#FF54FF",
                              fear="#009600",happiness="#FFFF54", sadness="#5151FF",surprise="#59BDFF")) +
  theme_bw(base_size = 12, base_family = "Trebuchet MS") + 
  ggtitle("Michel Temer Emotions During Address to\nNation After Bribery Accusations") +
  ylab("Intensity") + xlab("Video duration [seconds]") +
  theme(plot.title = element_text(family = "Trebuchet MS", color="#000000", face="bold", size=14, hjust=0.5)) +
  theme(axis.title = element_text(family = "Trebuchet MS", color="#000000", size=12)) +
  theme(aspect.ratio = 0.5)
  
# ======= Smoothing method: loess ===========
smooth_plot <- ggplot(df, aes(seconds)) +
  geom_smooth(aes(y = anger, colour = "anger"), method="loess") +
  geom_smooth(aes(y = contempt, colour = "contempt"), method="loess") +
  geom_smooth(aes(y = disgust, colour = "disgust"), method="loess") +
  geom_smooth(aes(y = fear, colour = "fear"), method="loess") +
  geom_smooth(aes(y = happiness, colour = "happiness"), method="loess") +
  geom_smooth(aes(y = sadness, colour = "sadness"), method="loess") +
  geom_smooth(aes(y = surprise, colour = "surprise"), method="loess") +
  scale_color_manual(values=c(anger="#FF3333",contempt="#C20084",disgust="#FF54FF",
                              fear="#009600",happiness="#FFFF54", sadness="#5151FF",surprise="#59BDFF")) +
  theme_bw(base_size = 12, base_family = "Trebuchet MS") + 
  ggtitle("Michel Temer Emotions During Address to\nNation After Bribery Accusations") +
  ylab("Intensity") + xlab("Video duration [seconds]") +
  theme(plot.title = element_text(family = "Trebuchet MS", color="#000000", face="bold", size=14, hjust=0.5)) +
  theme(axis.title = element_text(family = "Trebuchet MS", color="#000000", size=12)) +
  theme(aspect.ratio = 0.5)

ggsave(filename = "temer_emotions.png", plot = smooth_plot)
