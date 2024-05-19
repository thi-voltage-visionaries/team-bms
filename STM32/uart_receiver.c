#include "stm32f4xx_hal.h"

#define UART_BUFFER_SIZE 10000 //10kbyte SRAM

UART_HandleTypeDef huart2; //Handler for UART transceive and receive

void SystemClock_Config(void); //Configuration system cycle time
static void MX_GPIO_Init(void); //Configuration GPIO-pins for UART
static void MX_USART2_UART_Init(void); //Configuration UART-peripheral

void SystemClock_Config(void) {

}

static void MX_GPIO_Init(void) {

}

void HAL_UART_RxCplt-Callback(UART_HandleTypeDef *huart) {

}

static void MX_USART2_UART_Init(void) {
    huart2.Instance             = USART2                //Schnittstelle
    huart2.Init.Baudrate        = 115200;               //Übertragung Bit pro Sekunde typsicherweise 115200
    huart2.Init.WordLength      = UART_WORDLENGTH_8B;   //Anzahl der Bits für jedes Datenwort typischerweise 8 Bit
    huart2.Init.StopBits        = UART_STOPBITS_1;      //Werden am Ende jedes Datenwortes übertragen typischerweise 1 Bit
    huart2.Init.Parity          = UART_PARITY_NONE;     //Fehlererkennungsverfahren None, Even (Gerade) oder Odd (Ungerade)
    huart2.Init.Mode            = UART_MODE_RX;         //Modus der UART-Schnittstelle Rx Tx
    huart2.Init.HwFlowCtl       = UART_HWCONTROL_NONE;  //Steuerung des Hardwareflusses zwischen Sender und Empfänger None, RTS, RTS/CTS-Flusskontrolle
    huart2.Init.OverSampling    = UART_OVERSAMPLING_16; //Anzahl der Samples pro Bit typischerweise 16 Samples pro Bit
}

int main(void) {
    uint8_t rx_data[UART_BUFFER_SIZE];

    HAL_Init();
    SystemClock_Config();
    MX_GPIO_Init();
    MX_USART2_UART_Init();

    while(1) {
        HAL_UART_Receive(&huart2, rx_data, 10, HAL_MAX_DELAY); //Receiver
        //Processing received data
        //Manage content from data buffer
        HAL_UART_Transmit(&huart2, rx_data, 10, HAL_MAX_DELAY); //Transmitter
    }
}
