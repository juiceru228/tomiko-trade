FROM node

WORKDIR /client
COPY ./client /client
RUN npm i
COPY . .
CMD ["npm", "run", "serve"]

