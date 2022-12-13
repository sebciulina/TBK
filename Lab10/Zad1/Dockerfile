FROM node:alpine

ENV MAX_ALLOCATION_MB=4096 \
    LOOP_ALLOCATION_MB=512 \
    LOOP_INTERVAL_MS=2000

RUN free -m | grep 'Mem:' | awk '{if($4 < MAX_ALLOCATION_MB){print "Not enough memory available"; exit 1}}'

WORKDIR /app
COPY src/ .

HEALTHCHECK --interval=5s --timeout=1s --retries=1 --start-period=5s CMD node memory-check.js

CMD ["node", "memory-hog.js"]
