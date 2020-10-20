FROM node:12.19.0-slim

RUN npm install -g @vue/cli
RUN npm install -g @vue/cli-service

RUN mkdir /app

WORKDIR /app

COPY package*.json ./

RUN npm install

EXPOSE 8080

ADD . .