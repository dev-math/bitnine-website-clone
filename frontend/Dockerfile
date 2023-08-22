FROM node:18-alpine

WORKDIR /opt/frontend

COPY ./package.json ./package-lock.json .
RUN npm install

COPY . .
