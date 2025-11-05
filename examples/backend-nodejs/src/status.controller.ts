import { Controller, Get } from '@nestjs/common';

@Controller()
export class StatusController {
  @Get('health')
  health() {
    return { status: 'ok' };
  }
}
