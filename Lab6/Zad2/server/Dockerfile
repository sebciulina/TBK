FROM node:latest as build
WORKDIR /app
COPY package.json ./
RUN npm install
COPY . .

FROM node:alpine3.16
WORKDIR /app
COPY --from=build /app .
EXPOSE 9000
CMD node server.js