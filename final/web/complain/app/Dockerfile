FROM node:16-alpine

RUN adduser -D anonim

WORKDIR /home/anonim/app

COPY . .

# Installs latest Chromium (100) package.
RUN apk add --no-cache \
      chromium \
      nss \
      freetype \
      harfbuzz \
      ca-certificates \
      ttf-freefont

# Tell Puppeteer to skip installing Chrome. We'll be using the installed package.
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

RUN npm install
# RUN npm install -g nodemon
USER anonim

EXPOSE 21204

# CMD ["nodemon","index.js"]

CMD [ "npm", "start"]