import { IsNotEmpty, IsString, MaxLength } from 'class-validator';

export class CreateChatDto {
  @IsString()
  @IsNotEmpty()
  @MaxLength(1000)
  message!: string;
}
