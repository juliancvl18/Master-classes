Z0 <- 0.5
Tmax <- 300

epsilon_Tmax1 <- rnorm(Tmax,0,1)
epsilon_Tmax2 <- rnorm(Tmax,0,1)

Xtplus <- Z0 + cumsum(epsilon_Tmax1)
Xtplus1 <- Z0 + cumsum(epsilon_Tmax2)

y1 <- c(Z0, Xtplus)
#y1[y1 <= 0] <- 0
y2 <- c(Z0, Xtplus1)

x = 0: Tmax

windowsFonts(A = windowsFont("Times New Roman"))
plot(x = x, xlab = "Generations", y = y1, ylab = "Allele Frequency", family="A", type = 'l')
lines(x = x, y = y2, col = "red")


