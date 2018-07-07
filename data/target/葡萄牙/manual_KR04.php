<?php 
 	 $textConfig = ["消息推送" =>"Envio de mensagem",
"安卓设备在首次使用时会提示多种权限设置，请给予LinkTo所有权限，权限的缺失又可能导致手机结束应用进程，从而导致部分数据不完整。" =>"Os dispositivos Android solicitarão várias configurações de permissão quando forem usados ​​pela primeira vez.Por favor, forneça a LinkTo todas as permissões.A falta de permissões pode fazer com que o telefone celular termine o processo de inscrição, resultando em alguns dados incompletos.",
"第一次使用设备时没有给予消息推送的权限，之后再给予权限，可能导致消息不能正常推送，出现此类情况时，请将设备与应用断开连接然后再次连接，消息就能够正常提示。" =>"Na primeira vez que você usa o dispositivo, você não dá permissão para enviar a mensagem.Depois de dar permissão, a mensagem pode não ser enviada corretamente.Quando ocorrer uma situação como essa, desconecte o dispositivo do aplicativo e conecte-o novamente, e a mensagem será solicitada.",
"扫码无法识别" =>"O código de verificação não é reconhecido",
"首先检查手表是否还有电，请先查看手表屏幕是否能点亮，若不能点亮，请先给手表充电后再尝试连接，若手表有点，请尽可能的将手表贴近手机后重试。若以上操作后仍然无法连接，请尝试开关一次手机蓝牙或者重启手机。" =>"Primeiro verifique se o relógio ainda tem eletricidade. Verifique se a tela do relógio pode ser acesa. Se não puder ser acesa, carregue o relógio antes de tentar se conectar.Se o relógio for um pouco, tente fechar o relógio no telefone e tente novamente. ",
"先关闭扫码页面，再次尝试扫描，如若连接不上，可尝试手动连接" =>"Primeiro, desative a página de códigos de verificação e tente digitalizar novamente. Se não conseguir se conectar, tente conectar-se manualmente.",
"如若以上步骤都尝试后，建议将手表重启，再次连接。" =>"Se você já tentou todas as etapas acima, é recomendável reiniciar o relógio e conectar-se novamente.",
"手机来电为什么手表没有提醒" =>"Por que não há lembretes no telefone?",
"1.来电提醒、短信提醒、APP通知提醒功能需要一直开启手机蓝牙，保持手表与手机的连接。" =>"1. Lembrete de chamada, lembrete de SMS, função de lembrete de notificação APP precisa sempre ligar o celular Bluetooth, manter a conexão entre o relógio eo telefone celular.",
"2.计步、心率等不需要一直开启蓝牙，使用时只需要佩戴手表，使用完成后将手表与手机同步查看数据即可。" =>"2. Contagem de passos, ritmo cardíaco, etc. Não precisa de ligar o Bluetooth sempre, só precisa de usar o relógio quando o utiliza Depois de o utilizar, pode ver os dados em sincronia com o telefone.",
"设置来电提醒时，需要保持手机蓝牙一直处于开启状态，请先检查手机蓝牙是否打开且与手表连接成功。" =>"Ao definir o alerta de chamada, você precisa manter o Bluetooth do telefone ligado.Por favor, verifique se o Bluetooth está ligado e conectado ao relógio.",
"怎么选择手表接收指定应用提醒" =>"Como escolher um relógio para receber um lembrete de aplicativo específico",
"1.对于设置了通知的相关APP，请确保手机是否已经允许“手机通知”。" =>"1. Para aplicativos relacionados com notificações definidas, certifique-se de que o telefone tenha permitido \"Notificação móvel\".",
"2.手表需要和手机保持连接，蓝牙需要保持开启状态。" =>"2. O relógio precisa estar conectado ao telefone e o Bluetooth precisa permanecer ligado.",
"安卓用户进入app设备页面，点击通知提醒，选择需要的应用打开提醒开关。" =>"Os usuários do Android entram na página do dispositivo do aplicativo, clicam no lembrete de notificação e selecionam o aplicativo desejado para abrir a opção de lembrete.",
"ios用户默认全部打开。" =>"O usuário do ios está aberto por padrão.",
"为什么切换手环／手表连接手机步数没有同步" =>"Por que não há sincronização entre a comutação da conexão bracelete / relógio?",
"当手机蓝牙打开且打开LinkTo时，app会自动同步数据，同时也可以在各页面下拉数据列表进行手动同步。" =>"Quando o telefone Bluetooth está ligado e o LinkTo está ligado, o aplicativo sincroniza automaticamente os dados e você também pode sincronizar manualmente a lista de dados em cada página.",
"连接正常的情况下，切换的手环／手表的步数小于上一台连接设备的步数时，那么步数将不再刷新，取最大值" =>"Quando a conexão estiver normal, quando o número de etapas da pulseira comutada / relógio for menor que o número de etapas do dispositivo conectado anterior, o número de etapas não será atualizado e o valor máximo será alcançado.",
"如何设置计步目标" =>"Como definir uma meta no contador de etapas",
"若同步时提示连接失败，可先下拉数据列表进行手动同步调节，如果无效，请结束app进程，再重新进入。" =>"Se a conexão falhar durante a sincronização, primeiro você pode puxar para baixo a lista de dados para executar o ajuste de sincronização manual.Se ela for inválida, por favor, finalize o processo do aplicativo e entre novamente.",
"若以上步骤后仍不能同步，请开关一次蓝牙手机或重启手机。" =>"Se você ainda não conseguir sincronizar após as etapas acima, troque o telefone Bluetooth uma vez ou reinicie o telefone.",
"点击个人中心-设置目标，选择自己的目标步数然后保存。" =>"Clique em Personal Center - Definir metas, selecione suas próprias etapas de destino e salve.",
"步数为什么和我的微信数据不一样" =>"Por que o número de etapas é diferente dos meus dados do WeChat?",
"LinkTo不会获取手机本身的运动数据，软件内的步数数据只来自手表，当手表没有记录时，app上将不会有步数的数据。" =>"O LinkTo não obtém os dados de movimento do próprio telefone. Os dados do passo no software só vêm do relógio. Quando o relógio não está gravado, não haverá dados de etapa no aplicativo.",
"不同设备或者硬件都有不同的数据或传感器，所以数据会不尽相同，如果是正常活动，通常不会有太大偏差，不必担心。" =>"Dispositivos ou hardware diferentes têm dados ou sensores diferentes, portanto, os dados serão diferentes. Se for uma atividade normal, geralmente não há muito desvio, então não se preocupe.",
"安卓的权限设置" =>"Configurações de permissão do Android",
"iOS设备在首次使用时会提示多种权限设置，如果您需要获取一天完整的轨迹，则需要将GPS权限一直给予LinkTo,如果仅在使用期间允许，那么手机会在其他时间段将进程结束，这就会导致您无法获取完整轨迹或无轨迹。" =>"Os dispositivos iOS solicitarão várias configurações de permissão quando forem usados ​​pela primeira vez.Se você precisar obter uma faixa completa do dia, precisará dar permissão ao GPS para Vincular o tempo todo.Se isso for permitido somente durante o uso, o telefone encerrará o processo em outros períodos. ",
"安卓设备在首次使用时会提示多种权限设置，请给予LinkTo所有权限，权限的缺失又可能导致手机结束应用进程，从而导致部分数据不完整。" =>"Os dispositivos Android solicitarão várias configurações de permissão quando forem usados ​​pela primeira vez.Por favor, forneça a LinkTo todas as permissões.A falta de permissões pode fazer com que o telefone celular termine o processo de inscrição, resultando em alguns dados incompletos.",
];