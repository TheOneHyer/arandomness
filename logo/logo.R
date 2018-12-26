# Create logo for arandomness

# Load necessary libraries
library(ggplot2)

# Reproducibility
set.seed(3284)

# Generate data clusters and bind into a data frame
x <- cbind(rnorm(500, mean = 0, sd = 1), rnorm(500, mean = 0, sd = 1), rnorm(500, mean = 0, sd = 0.005))
y <- cbind(rnorm(500, mean = 10, sd = 1), rnorm(500, mean = 0, sd = 1), rnorm(500, mean = 1, sd = 0.005))
z <- cbind(rnorm(500, mean = 5, sd = 1), rnorm(500, mean = sqrt(3)/2*5, sd = 1), rnorm(500, mean = 0.5, sd = 0.005))
d <- data.frame(rbind(x, y, z))

# Create plot with line segments and no axes, legends, etc.
p <- ggplot(d, aes(x = X1, y = X2, color = X3)) +
  geom_point() +
  scale_color_gradientn(colors = c("green", "red", "blue"),
                        values = c(0, 0.5, 1)) +
  geom_segment(aes(x = 0, y = 0, xend = 10, yend = 0), color = "red", lineend = "round", size = 2) +
  geom_segment(aes(x = 10, y = 0, xend = 5, yend = sqrt(3)/2*5), color = "green", lineend = "round", size = 2) +
  geom_segment(aes(x = 5, y = sqrt(3)/2*5, xend = 0, yend = 0), color = "blue", lineend = "round", size = 2) +
  theme(axis.line = element_blank(), axis.text.x = element_blank(),
        axis.text.y = element_blank(), axis.ticks = element_blank(),
        axis.title.x = element_blank(), axis.title.y = element_blank(),
        legend.position = "none", panel.background = element_blank(),
        panel.border = element_blank(), panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(), plot.background = element_blank())

# Save logo in multiple sizes and display it
png(filename = "arandomness_logo_160.png", width = 160, height = 160)
p
dev.off()

png(filename = "arandomness_logo_480.png", width = 480, height = 480)
p
dev.off()

png(filename = "arandomness_logo_512.png", width = 512, height = 512)
p
dev.off()

png(filename = "arandomness_logo_720.png", width = 720, height = 720)
p
dev.off()

p
