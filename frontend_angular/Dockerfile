# Frontend Dockerfile
FROM node:16

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY ./frontend/package*.json /app/
RUN npm install

# Copy the rest of the application code
COPY ./frontend /app/

# Expose the port Angular will run on
EXPOSE 4200

# Start the Angular application
CMD ["npm", "start"]
