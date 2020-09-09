# Run

```
docker run --rm -it --name locust \
-p 8089:8089 \
--env INDEX=/ \
--env MIN_WAIT=3 \
--env MAX_WAIT=5 \
cuongnb14/locust:0.1
```