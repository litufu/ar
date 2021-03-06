import React from 'react';
import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './index.css';
import { Upload, message, Button } from 'antd';

import { UploadOutlined } from '@ant-design/icons';

const props = {
  name: 'file',
  action: 'http://localhost:8080/upload',
  headers: {
    authorization: 'authorization-text',
  },
  onChange(info) {
    if (info.file.status !== 'uploading') {
      console.log(info.file, info.fileList);
    }
    if (info.file.status === 'done') {
      message.success(`${info.file.name} file uploaded successfully`);
    } else if (info.file.status === 'error') {
      message.error(`${info.file.name} file upload failed.`);
    }
  },
};

ReactDOM.render(
  <Upload {...props}>
    <Button icon={<UploadOutlined />}>Upload Directory</Button>
  </Upload>,
  document.getElementById('root'),
);