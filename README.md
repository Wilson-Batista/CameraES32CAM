## CameraES32CAM
# Dependencias da aplicação
CameraIP
1. Flask: Uma estrutura da web em Python para execução do script index.html
```
pip install Flask
```
2. OpenCV (cv2): Uma biblioteca de visão computacional em código aberto que possibilita capturar, processar e analisar video em tempo real.
```
=======
```OpenCV (cv2): Uma biblioteca de visão computacional em código aberto
>>>>>>> parent of f537dfc (Update README.md)
pip install opencv-python
```
3. NumPy: Uma biblioteca que possibilita a realização de operaçoes matematicas em arrays multidimensionais, utilizado para converter os bytes dos flames em um array do tipo de 8 bits.
```
pip install numpy
```
4. ImageIO: Uma biblioteca que possibilita ler, gravar imagens e videos em varios formatos com o proposito de ser simples sem se preocupar com o formato do arquivo.
```
pip install imageio
```
5. Ngrok: E uma ferramenta que possibilita o acesso publico a servidores ou serviço locais mesmo estando tras de forewals ou roteadores, fornecendo links url publico que redireciona o trafego ao servidor local.
Baixar o Ngrok ubuntu.
```
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

```
6. descompactar Ngrok.
```
unzip ngrok-stable-linux-amd64.zip

```
7. Movendo o executavel e sua variavel para pasta bin
```
sudo mv ngrok /usr/local/bin/
```
8. Execução da aplicação
```
ngrok http 5000
```
