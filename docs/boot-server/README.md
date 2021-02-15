# Tateru boot services

## Installing a PXE server

```
ansible-playbook -i 172.16.31.90, \
  give-me-a-pxe-server.yml \
  -e TATERU_ISO="${HOME}/tateru-installer/build/out/tateru-boot.iso" \
  -e TATERU_SVC=http://172.16.31.10:7865 \
  -e TATERU_BOOT_URL=http://172.16.31.90
```
