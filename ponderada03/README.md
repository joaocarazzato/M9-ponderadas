
# Vulnerabilidades em dispositivos MQTT segundo a CIA Triad
O objetivo deste repositório é analisar as potenciais vulnerabilidades de segurança associadas a dispositivos MQTT utilizando os princípios da CIA Triad. Levando em consideração os pilares de confidencialidade, integridade e disponibilidade.

## Confiabilidade
A falta de uma configuração adequada de autenticação e autorização de clientes MQTT pode resultar em acessos não autorizados no sistema, o que poderia permitir a publicação ou acesso a informações sensíveis.


## Integridade
A ausência de criptografia e a falta de validação adequada das mensagens recebidas podem abrir portas para ataques de Man-in-the-Middle, que permitem a interceptação e modificação das mensagens, bem como o envio de mensagens maliciosas



## Disponibilidade
O servidor MQTT pode ser alvo de ataques de negação de serviço (DoS), os quais sobrecarregam o servidor, resultando na indisponibilidade do serviço para os clientes.

### Possíveis soluções
* Criptografia dos dados durante a comunicação para manter a confidencialidade e a integridade.
* Implementar um serviço de autenticação e autorização para os clientes utilizando certificados digitais
* Criar políticas de acesso para limitar que pode publicar e acessar tópicos determinados do MQTT.


## Conclusão
A análise de vulnerabilidades de dispositivos MQTT revelou várias situações em que a segurança, integridade e disponibilidade são comprometidas. Ao implementar as soluções possíveis, essas vulnerabilidades são mitigadas, aproximando-nos de um ambiente mais seguro para dispositivos MQTT.
