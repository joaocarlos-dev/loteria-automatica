import React from 'react';
import { Row, Col, Input, Button, Form } from 'antd';
import './App.css';

function msgButton(buttonName){
  alert("Clicou no botão: " + buttonName);
}

const App = () => (
  <Row justify='center' align='middle'>
    <Form layout='vertical'>
      <Form.Item label="Quantidade de jogadores: ">
        <Input type={"number"}></Input>
      </Form.Item>
      <Form.Item>
        <Button
          type="primary"
          block
          onClick={() => msgButton(1)}>
            Novo Jogo
        </Button>
      </Form.Item>
    </Form>
  </Row>
);

export default App;