## Steps

```bash
docker run --interactive --tty --rm \
--mount type=bind,source=$(pwd),target=/home/neo \
almalinux8p10_build
```
